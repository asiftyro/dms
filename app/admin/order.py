from flask import Blueprint, render_template, redirect, url_for
# from flask_login import current_user
# from ..models import MERCHANT_ROLES, ADMIN_ROLES

admin_order = Blueprint('admin_order', __name__, template_folder='')


@admin_order.route('/', methods=['GET'])
def view():
    return "admin view order"