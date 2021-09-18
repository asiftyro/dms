from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from ..models import MERCHANT_ROLES, ADMIN_ROLES
home = Blueprint('home', __name__, template_folder='')


@home.route('/', methods=['GET'])
def homepage():
    # TODO: implement this inside auth.login.
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    elif current_user.role in MERCHANT_ROLES:
        return redirect(url_for('order.view_order'))
    elif current_user.role in ADMIN_ROLES:
        return redirect(url_for('admin_order.order'))
