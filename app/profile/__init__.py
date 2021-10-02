from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import current_user
from datetime import datetime

from ..models import Merchant, Role
from .forms import MerchantProfilePrimaryUpdateForm, MerchantProfileContactsUpdateForm, merchant_profile_update_forms
from app import db
from ..auth import role_required

profile = Blueprint('profile', __name__, template_folder='')

PROFILE_PAGES = [key for key in merchant_profile_update_forms.keys()]
# PROFILE_PAGES.append('an_uneditable_profile_page')


def get_page_name_or_abort404():
    page = "primary" if "page" not in request.args else request.args.get("page")
    return page if page in PROFILE_PAGES else abort(404)


@profile.route('/', methods=['GET'])
@role_required(role=Role.MERCHANT_OWNER)
def read():
    page = get_page_name_or_abort404()
    model = Merchant.query.filter_by(id=current_user.merchant_id).first()
    return render_template('profile.html', title="Merchant Profile", profile_pages=PROFILE_PAGES, view=page, edit=False,
                           data=model)


@profile.route('/update', methods=['GET', 'POST'])
@role_required(role=Role.MERCHANT_OWNER)
def update():
    page = get_page_name_or_abort404()
    model = Merchant.query.filter_by(id=current_user.merchant_id).first()
    form = merchant_profile_update_forms[page](obj=model)
    form_validated = False

    if form.validate_on_submit():
        for fieldname, value in form.data.items():
            if fieldname in ['submit', 'csrf_token']: continue
            setattr(model, fieldname, form[fieldname].data)
        form_validated = True

    if form_validated:
        model.modified_by = current_user.id
        db.session.commit()
        flash('You have successfully updated your Profile.', 'success')
        return redirect(url_for('profile.read', page=page))
    else:
        return render_template('profile.html', title="Edit Merchant Profile", profile_pages=PROFILE_PAGES, view=page,
                               data=model, edit=True, form=form)
