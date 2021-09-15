from flask import Blueprint, flash, redirect, render_template, url_for, abort
from flask_login import login_required, login_user, logout_user, current_user

from app import db
from .form import LoginForm, RegistrationForm
from ..models import User, UserType, Merchant
from .roles import merchant_required, admin_required, role_required
from ..utils import send_async_email

auth = Blueprint('auth', __name__, template_folder='')


@auth.route('/login', methods=['GET', 'POST'])
@role_required(role=None)
def login():



    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            if user.is_active():  # todo: add email_confirmed clause
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
@role_required(role=None)
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

        # TODO: Send mail
        # send_async_email(
        #     user_obj.email,
        #     'Activate your Ural Account.',
        #     'Welcome! Please copy the following link and paste it to your browser address bar, then press enter. {'
        #     'activation_link}'.format(activation_link=''),
        #     '<b>My HTML message</b>')

        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth.html', form=form, title='Register', view="register")


# TODO: @auth.route('/verify-email', methods=['GET'])
@auth.route('/verify-email', methods=['GET'])
def verify_email():
    return 'verify email page'


# TODO: @auth.route('/reset-password', methods=['GET', 'POST'])
@auth.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    return 'reset password page page'


# TODO: @auth.route('/reset/<token>', methods=["GET", "POST"])
@auth.route('/reset/<token>', methods=["GET", "POST"])
def reset_pass_with_token(token):
    pass
