from flask import Blueprint, render_template, redirect, url_for

# from flask_login import current_user
# from ..models import MERCHANT_ROLES, ADMIN_ROLES

admin_user = Blueprint('admin_user', __name__, template_folder='')


@admin_user.route('/', methods=['GET'])
def view():
    return "admin view user"
