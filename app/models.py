# app/models.py
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.mysql import INTEGER, BIGINT

from app import db, login_manager
from enum import Enum


class Role(Enum):
    """
    Type of users
    """
    MERCHANT_OWNER = 1
    MERCHANT_USER = 2
    ADMIN_SUPER = 3
    ADMIN_MANAGER = 4
    ADMIN_USER = 5


MERCHANT_ROLES = [Role.MERCHANT_OWNER, Role.MERCHANT_USER]
ADMIN_ROLES = [Role.ADMIN_USER, Role.ADMIN_MANAGER, Role.ADMIN_SUPER]


class OrderStatus(Enum):
    """
    Status of orders
    """
    CREATED = 1
    CANCELLED_BY_MERCHANT = 2
    CANCELLED_BY_ADMIN = 3
    PROCESSING = 4
    SHIPPED = 5
    RECEIVED = 6
    RETURNED_BY_CUSTOMER = 7
    RETURNED_BY_ADMIN = 7


class PaymentStatus(Enum):
    """
    Payment status of orders
    """
    UNPAID = 0
    PAID = 1


class User(UserMixin, db.Model):
    """
    Users table
    """
    __tablename__ = 'users'

    id = db.Column(BIGINT(unsigned=True, zerofill=True), primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    merchant_id = db.Column(db.Integer, nullable=False)
    role = db.Column(db.Enum(Role), nullable=False, default=Role.MERCHANT_OWNER)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    email_confirmed=db.Column(db.Boolean(), nullable=False, default=False)

    # is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return self.active

    def is_email_confirmed(self):
        return self.email_confirmed

    def is_merchant(self):
        return self.role in MERCHANT_ROLES

    def is_admin(self):
        return self.role in ADMIN_ROLES

    def __repr__(self):
        return '<User: {}>'.format(self.id)


class Order(db.Model):
    """
    Model for table 'orders'
    """
    __tablename__ = 'orders'

    id = db.Column(BIGINT(unsigned=True, zerofill=True), primary_key=True)
    merchant_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    status = db.Column(db.Enum(OrderStatus), nullable=False, default=OrderStatus.CREATED)
    payment_status = db.Column(db.Enum(PaymentStatus), nullable=False, default=PaymentStatus.UNPAID)

    def __repr__(self):
        return '<Order: {}>'.format(self.id)


class Merchant(db.Model):
    """
    Merchant model
    """
    __tablename__ = 'merchants'
    id = db.Column(BIGINT(unsigned=True, zerofill=True), primary_key=True)
    merchant = db.Column(db.String(128))
    active = db.Column(db.Boolean(), nullable=False, default=True)

    def __repr__(self):
        return '<Merchant: {}>'.format(self.id)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
