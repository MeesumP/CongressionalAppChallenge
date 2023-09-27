import path, os

from flask import Flask
from views import views
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from models import db, DB_NAME

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')

    from models import User

    create_database(app)

    return app


def create_database(app):
    if not os.path.isfile('website/' + DB_NAME):
        pass