from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user
from datetime import datetime

from ..models import Merchant, Role
from .forms import MerchantProfileEditForm
from app import db
from ..auth import role_required

profile = Blueprint('profile', __name__, template_folder='')


@profile.route('/', methods=['GET'])
@role_required(role=Role.MERCHANT_OWNER)
def view():
    data = Merchant.query.filter_by(id=current_user.merchant_id).first()
    return render_template('profile.html', title="Merchant Profile", view='single', data=data)


@profile.route('/edit', methods=['GET', 'POST'])
@role_required(role=Role.MERCHANT_OWNER)
def edit():
    data = Merchant.query.filter_by(id=current_user.merchant_id).first()
    form = MerchantProfileEditForm(obj=data)
    if form.validate_on_submit():
        data.name = form.name.data
        data.address = form.address.data
        data.modified_by = current_user.id
        data.modified_at = datetime.now()
        db.session.commit()
        flash('You have successfully updated your Profile.', 'success')
        return redirect(url_for('profile.view'))

    return render_template('profile.html', title="Edit Merchant Profile", view='edit', data=data, form=form)
