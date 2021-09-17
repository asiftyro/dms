from flask import Blueprint, flash, redirect, render_template, url_for, current_app, abort
from flask_login import login_required, login_user, logout_user, current_user
from datetime import datetime
from app import db
from .form import LoginForm, RegistrationForm
from ..models import User, Role, Merchant
from .roles import merchant_required, admin_required, role_required
from ..utils import send_async_email, get_email_token, check_email_token

auth = Blueprint('auth', __name__, template_folder='')


@auth.route('/login', methods=['GET', 'POST'])
@role_required(role=None)
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            if not user.is_email_confirmed():
                fmsg = "Your account is not active. Please click the activation link sent to your email to activate " \
                       "your account. "
                flash(fmsg, 'danger')
                return redirect(url_for('auth.login'))
            if user.is_active():
                login_user(user)
                flash('Login Succesful. Welcome!', 'success')
                return redirect(url_for('home.homepage'))
            else:
                flash("Account is not active. Contact Administrator", "danger")
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('auth.html', form=login_form, title="Login", view="login")


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
@role_required(role=None)
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        user_obj = User(
            email=reg_form.email.data,
            first_name=reg_form.first_name.data,
            last_name=reg_form.last_name.data,
            password=reg_form.password.data,
            role=Role.MERCHANT_OWNER,
        )
        db.session.add(user_obj)
        db.session.flush()

        merchant = Merchant(
            created_by=user_obj.id,
            created_at=datetime.now()
        )
        db.session.add(merchant)
        db.session.flush()

        user_obj.merchant_id = merchant.id
        user_obj.created_by = user_obj.id
        db.session.add(user_obj)
        db.session.commit()

        token = get_email_token(email=user_obj.email)
        confirm_url = url_for('auth.verify_email', token=token, _external=True)
        subject = "Activate your Ural account."
        html = render_template('email_templates/activate-account.html', confirm_url=confirm_url)
        txt = "Your account was successfully created. Please click the link below to confirm your email address and " \
              "activate your account: {link}".format(link=confirm_url)
        send_async_email(to=user_obj.email, subject=subject, message_text=txt, message_html=html,
                         sender=current_app.config['MAIL_USERNAME'])
        flash('Your account was successfully created. A link is sent to your email to activate your account.')
        return redirect(url_for('auth.login'))
    return render_template('auth.html', form=reg_form, title='Register', view="register")


@auth.route('/verify-email/<token>', methods=['GET'])
def verify_email(token):
    try:
        email = check_email_token(token)
        user = User.query.filter_by(email=email).first()
        if not user:
            raise Exception("Invalid or expired activation link used.")
        if user.email_confirmed:
            raise Exception("Invalid or expired activation link used.")
        user.email_confirmed = True
        db.session.commit()
        flash("Account activated succesfully.", "success")
        return redirect(url_for('auth.login'))
    except:
        flash("Invalid or expired activation link used.", "danger")
        abort(404)


# TODO: @auth.route('/reset-password', methods=['GET', 'POST'])
@auth.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    return 'reset password page'


# TODO: @auth.route('/reset/<token>', methods=["GET", "POST"])
@auth.route('/reset/<token>', methods=["GET", "POST"])
def reset_pass_with_token(token):
    return 'reset password page'
