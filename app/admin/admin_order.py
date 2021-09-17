from flask import Blueprint, render_template, redirect, url_for, request, jsonify
# from flask_login import current_user
from datatables import ColumnDT, DataTables
from sqlalchemy import func
from ..models import MERCHANT_ROLES, ADMIN_ROLES, Order, Merchant, User
from app import db

admin_order = Blueprint('admin_order', __name__, template_folder='')


@admin_order.route('/', methods=['GET'])
def order():
    return render_template('admin_order.html', title='Manage Orders')


@admin_order.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit(order_id=None):
    return "HJ"


@admin_order.route("/orders")
def orders():
    c = [
        ColumnDT(User.id),
        ColumnDT(User.id),
        ColumnDT(User.email)
    ]

    query = db.session.query().select_from(User)

    # GET parameters
    params = request.args.to_dict()
    if "start" not in params: params["start"] = 0
    if "length" not in params: params["length"] = -1

    row_table = DataTables(params, query, c)

    return jsonify(row_table.output_result())
