from flask import Blueprint, flash, redirect, render_template, url_for, abort
from flask_login import login_required, login_user, logout_user, current_user
import functools

from .form import LoginForm, RegistrationForm
from ..models import User, UserType, Merchant
from app import db

auth = Blueprint('auth', __name__, template_folder='')


def merchant_user_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if current_user.user_type not in [UserType.MERCHANT_OWNER, UserType.MERCHANT_USER]:
            abort(403)
        return view(**kwargs)

    return wrapped_view


def admin_user_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if current_user.user_type in [UserType.MERCHANT_OWNER, UserType.MERCHANT_USER]:
            abort(403)
        return view(**kwargs)

    return wrapped_view


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            if user.is_active():   # todo: add email_confirmed clause
                login_user(user)
                flash('Login Succesful. Welcome!', 'success')
                return redirect(url_for('order.view_order'))  # todo: redicrect at different endpoint based on user type
            else:
                flash("Account is not active. Contact Administrator", "danger")
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('auth.html', form=form, title="Login", view="login")


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        merchant = Merchant()
        db.session.add(merchant)
        db.session.flush()
        user_obj = User(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data,
            merchant_id=merchant.id,
            user_type=UserType.MERCHANT_OWNER,
        )

        db.session.add(user_obj)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth.html', form=form, title='Register', view="register")
