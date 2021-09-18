from flask import Blueprint, render_template, redirect, url_for, request, jsonify, abort, flash
from datetime import datetime
from datatables import ColumnDT, DataTables
from sqlalchemy import func
from flask_login import current_user, login_required
from ..auth import  role_required
from ..models import MERCHANT_ROLES, ADMIN_ROLES, Order, Merchant, User
from .forms import AdminOrderEditForm
from app import db

admin_order = Blueprint('admin_order', __name__, template_folder='')


@admin_order.route('/', methods=['GET'])
@admin_order.route('/<int:order_id>', methods=['GET'])
@login_required
@role_required(role=ADMIN_ROLES)
def order(order_id=None):
    if order_id is None:
        return render_template('admin_order.html', title='Manage Orders', view='all')
    else:
        data = Order.query.filter_by(id=order_id).first()
        return render_template('admin_order.html', title='Manage Order', view='single', data=data)


@admin_order.route('/edit/<int:order_id>', methods=['GET', 'POST'])
@login_required
@role_required(role=ADMIN_ROLES)
def edit(order_id):
    order_obj = Order.query.filter_by(id=order_id).first()
    if order_obj is None:
        flash('Order not found', 'warning')
        return redirect(url_for('admin_order.order'))
    form = AdminOrderEditForm(obj=order_obj)
    if form.validate_on_submit():
        order_obj.description = form.description.data
        order_obj.address = form.address.data
        order_obj.status = form.status.data.split('.')[-1]  # todo: redo using actual enum name->value
        order_obj.payment_status = form.payment_status.data.split('.')[-1] # todo: redo using actual enum name->value
        order_obj.modified_by = current_user.id
        db.session.commit()
        flash('You have successfully edited the Order.', 'success')
        return redirect(url_for('admin_order.order', order_id=order_id))
    return render_template('admin_order.html', title='Edit Order', view='edit', form=form, data=order_obj)


@admin_order.route("/orders")
@login_required
@role_required(role=ADMIN_ROLES)
def orders():
    c = [
        ColumnDT(Order.id),
        ColumnDT(Order.id),
        ColumnDT(Order.merchant_id),
        ColumnDT(Order.description),
        ColumnDT(Order.address),
        ColumnDT(Order.status),
        ColumnDT(Order.payment_status),
        ColumnDT(Order.created_by),
        ColumnDT(func.DATE_FORMAT(Order.created_at, '%Y-%m-%d %r')),
        ColumnDT(Order.modified_by),
        ColumnDT(func.DATE_FORMAT(Order.modified_at, '%Y-%m-%d %r'))
    ]

    query = db.session.query().select_from(Order)

    # GET parameters
    params = request.args.to_dict()
    if "start" not in params: params["start"] = '0'
    if "length" not in params: params["length"] = '-1'

    row_table = DataTables(params, query, c)

    return jsonify(row_table.output_result())
