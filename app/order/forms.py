from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField,SelectField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length


class OrderCreateForm(FlaskForm):
    """
    Order creation form for merchant users
    """
    description = StringField('Description', validators=[Length(min=1, max=128)])
    address = StringField('Address', validators=[Length(min=1, max=128)])
    submit = SubmitField('Add')


class OrderEditForm(FlaskForm):
    """
    Order creation form for merchant users
    """
    description = StringField('Description', validators=[Length(min=1, max=128)])
    address = StringField('Address', validators=[Length(min=1, max=128)])
    submit = SubmitField('Save')





