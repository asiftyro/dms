# app/auth/forms.py

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from config import Config
from ..models import User


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        Length(min=4, max=12),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm Password')
    # TODO: load config from instance if instance exist, otherwise use Config default
    if Config.RECAPTCHA_ENABLED:
        recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """

    user_email = StringField('Email', validators=[DataRequired(), Email()])
    user_password = PasswordField('Password', validators=[DataRequired()])
    # TODO: load config from instance if instance exist, otherwise use Config default
    if Config.RECAPTCHA_ENABLED:
        recaptcha = RecaptchaField()
    submit = SubmitField('Login')
