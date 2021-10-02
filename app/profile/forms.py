from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField,SelectField, BooleanField, ValidationError, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class MerchantProfilePrimaryUpdateForm(FlaskForm):
    """
    Merchant Profile Primary information Update Form
    """
    name = StringField('Merchant company name', validators=[Length(min=1, max=128)])
    trade_license = StringField('Trade license', validators=[Length(max=256)])
    website = StringField('Website', validators=[Length(max=256)])
    facebook = StringField('Facebook', validators=[Length(max=256)])
    contact_name = StringField("Primary/Owner contact's name", validators=[Length(max=128)])
    contact_designation = StringField("Primary/Owner contact's designation", validators=[Length(max=128)])
    contact_address = StringField("Primary/Owner contact's office address", validators=[Length(max=256)])
    contact_telephone = StringField("Primary/Owner contact's telephone", validators=[Length(max=32)])
    contact_email = StringField("Primary/Owner contact's email", validators=[Length(max=128)])
    alt_contact_name = StringField("Alternative contact's name", validators=[Length(max=128)])
    alt_contact_designation = StringField("Alternative contact's designation", validators=[Length(max=128)])
    alt_contact_address = StringField("Alternative contact's office address", validators=[Length(max=256)])
    alt_contact_telephone = StringField("Alternative contact's telephone", validators=[Length(max=32)])
    alt_contact_email = StringField("Alternative contact's email", validators=[Length(max=128)])

    submit = SubmitField('Save')


class MerchantProfileContactsUpdateForm(FlaskForm):
    """
    Merchant Profile Contacts information Update Form
    """
    billing_contact_name = StringField("Billing contact's name", validators=[Length(max=128)])
    billing_contact_designation = StringField("Billing contact's designation", validators=[Length(max=128)])
    billing_contact_address = StringField("Billing contact's office address", validators=[Length(max=256)])
    billing_contact_telephone = StringField("Billing contact's telephone", validators=[Length(max=32)])
    billing_contact_email = StringField("Billing contact's email", validators=[Length(max=128)])

    collection_contact_name = StringField("Collection contact's name", validators=[Length(max=128)])
    collection_contact_designation = StringField("Collection contact's designation", validators=[Length(max=128)])
    collection_contact_address = StringField("Collection contact's office address", validators=[Length(max=256)])
    collection_contact_telephone = StringField("Collection contact's telephone", validators=[Length(max=32)])
    collection_contact_email = StringField("Collection contact's email", validators=[Length(max=128)])

    submit = SubmitField('Save')


class MerchantProfileTnCAgreementForm(FlaskForm):
    tnc_agreed = BooleanField("I have read and agreed to the terms and conditions of service", default=False)
    submit = SubmitField('Save')


class MerchantProfileRateAgreementForm(FlaskForm):
    tnc_agreed = BooleanField("I have read and agreed to the rates and charges", default=False)
    submit = SubmitField('Save')


class MerchantProfileDocumentUploadForm(FlaskForm):
    tnc_agreed = FileField("Upload Document")
    submit = SubmitField('Save')


merchant_profile_update_forms = {
    'primary': MerchantProfilePrimaryUpdateForm,
    'contacts': MerchantProfileContactsUpdateForm,
    'tnc': MerchantProfileTnCAgreementForm,
    'rate': MerchantProfileRateAgreementForm,
    'document': MerchantProfileDocumentUploadForm,
}



