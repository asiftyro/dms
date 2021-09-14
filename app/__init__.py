# # app/__init__.py

# third-party imports
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# local imports
from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()


def error_404(e):
    return render_template('404.html'), 404


def error_403(e):
    return render_template('403.html'), 403


def error_500(e):
    return render_template('500.html'), 500


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.config.from_object(app_config[config_name])
    app.register_error_handler(404, error_404)
    app.register_error_handler(403, error_403)
    app.register_error_handler(500, error_500)
    db.init_app(app)
    CSRFProtect(app)
    Migrate(app, db)
    Bootstrap(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .home import home as home_bp
    app.register_blueprint(home_bp)

    from .profile import profile as profile_bp
    app.register_blueprint(profile_bp, url_prefix='/profile')

    from .order import order as order_bp
    app.register_blueprint(order_bp, url_prefix='/order')

    return app
