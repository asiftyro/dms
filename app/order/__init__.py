from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
import functools
from flask import abort

from app import db
from ..models import Order, OrderStatus, PaymentStatus, User, Role, MERCHANT_ROLES
from .forms import OrderCreateForm, OrderEditForm

from ..auth import merchant_required, admin_required, role_required

order = Blueprint('order', __name__, template_folder='')


@order.route('/', methods=['GET'])
@order.route('/<int:order_id>', methods=['GET'])
@login_required
@role_required(role=MERCHANT_ROLES)
def view_order(order_id=None):
    data = None
    if order_id is None:
        data = Order.query.filter_by(merchant_id=current_user.merchant_id).all()
        return render_template('order.html', title='Order List', view='all', data=data, model=Order)
    else:
        data = Order.query.filter_by(merchant_id=current_user.merchant_id, id=order_id).first()
        if data:
            return render_template('order.html', title='Order details', view='single', data=data)
        else:
            flash("You are not authorized to view this entry", 'warning')
            return redirect(url_for('order.view_order'))


@order.route('/add', methods=['GET', 'POST'])
@login_required
@role_required(role=MERCHANT_ROLES)
def add_order():
    form = OrderCreateForm()
    if form.validate_on_submit():
        # Todo: add user id in orders table
        order_obj = Order(address=form.address.data,
                          description=form.description.data,
                          merchant_id=current_user.merchant_id,
                          status=OrderStatus.CREATED,
                          created_by=current_user.id
                          )
        db.session.add(order_obj)
        db.session.commit()
        flash('Order Created.', 'success')
        return redirect(url_for('order.view_order'))
    return render_template('order.html', title='Add New Order', view='add', form=form)


@order.route('/edit/<int:order_id>', methods=['GET', 'POST'])
@login_required
@role_required(role=MERCHANT_ROLES)
def edit_order(order_id=None):
    order_obj = Order.query.filter_by(merchant_id=current_user.merchant_id, id=order_id).first()
    if order_obj is None:
        flash('You are not authorized to change this entry', 'warning')
        return redirect(url_for('order.view_order'))
    if order_obj.status != OrderStatus.CREATED:
        flash('This Order Cannot be Edited at this stage. Please contact admin.', 'info')
        return redirect(url_for('order.view_order', order_id=order_id))
    form = OrderEditForm(obj=order_obj)
    if form.validate_on_submit():
        order_obj.description = form.description.data
        order_obj.address = form.address.data
        order_obj.modified_by = current_user.id
        order_obj.modified_at = datetime.now()
        db.session.commit()
        flash('You have successfully edited the Order.', 'success')
        return redirect(url_for('order.view_order', order_id=order_id))
    return render_template('order.html', title='Edit Order', view='edit', form=form, data=order_obj)


@order.route('/cancel/<int:order_id>', methods=['POST'])
@login_required
@role_required(role=MERCHANT_ROLES)
def cancel_order(order_id=None):
    order_obj = Order.query.filter_by(merchant_id=current_user.merchant_id, id=order_id).first()
    if order_obj is None:
        flash('You are not authorized to change this entry', 'warning')
        return redirect(url_for('order.view_order'))

    if order_obj.status == OrderStatus.CREATED:
        order_obj.status = OrderStatus.CANCELLED_BY_MERCHANT
        order_obj.modified_by = current_user.id
        order_obj.modified_at = datetime.now()
        db.session.commit()
        flash('You have successfully Cancelled the Order.', 'success')
        return redirect(url_for('order.view_order', order_id=order_id))
    else:
        flash('This Order Cannot be Cancelled at this stage. Please contact admin.', 'info')
        return redirect(url_for('order.view_order', order_id=order_id))
