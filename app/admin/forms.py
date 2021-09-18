from flask_wtf import FlaskForm
from markupsafe import escape
from wtforms import PasswordField, StringField, SubmitField,SelectField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from ..models import OrderStatus, PaymentStatus


class AdminOrderEditForm(FlaskForm):
    """
    Order editing form for Admin users
    """
    description = StringField('Description', validators=[Length(min=1, max=128)])
    address = StringField('Address', validators=[Length(min=1, max=128)])
    status = SelectField('Status', choices=[(v, v.value) for v in OrderStatus],)
    payment_status = SelectField('Payment Status', choices=[(v, v.value) for v in PaymentStatus])
    submit = SubmitField('Save')





