import functools
from flask_login import current_user
from flask import abort
from ..models import UserType, MERCHANT_USER_TYPES, ADMIN_USER_TYPES


def role_required(role=None):
    def decorator(view):
        @functools.wraps(view)
        def decorated_function(*args, **kwargs):
            if role is None:
                abort(404)
            if current_user.is_authenticated and current_user.user_type not in role:
                abort(403)
            return view(**kwargs)

        return decorated_function

    return decorator


def merchant_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if current_user.user_type not in MERCHANT_USER_TYPES:
            abort(403)
        return view(**kwargs)

    return wrapped_view


def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if current_user.user_type in ADMIN_USER_TYPES:
            abort(403)
        return view(**kwargs)

    return wrapped_view
