from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField,SelectField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length


class MerchantProfileEditForm(FlaskForm):
    """
    Merchant profile updating form
    """
    name = StringField('Name', validators=[Length(min=1, max=128)])
    address = StringField('Address', validators=[Length(min=1, max=256)])
    submit = SubmitField('Save')






