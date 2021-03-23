"""_init_.py is used to define app and all blueprints"""
from datetime import timedelta
from flask import Flask

# from flask_login import LoginManager
#from db import db

def create_app():
    app = Flask(__name__)

    app.secret_key = 'heyheyhey'
    app.permanent_session_lifetime = timedelta(hours=24)
    app.config['SECRET_KEY'] = 'heyheyhey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import sample_bp
    app.register_blueprint(sample_bp.bp)


    db.init_app(app)
    return app