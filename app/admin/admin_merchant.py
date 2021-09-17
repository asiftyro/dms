from flask import Blueprint, render_template, redirect, url_for
# from flask_login import current_user
# from ..models import MERCHANT_ROLES, ADMIN_ROLES

admin_merchant = Blueprint('admin_merchant', __name__, template_folder='')


@admin_merchant.route('/', methods=['GET'])
def view():
    return "admin view merchant"