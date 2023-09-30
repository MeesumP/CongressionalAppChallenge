from os import path

from flask import Flask
from views import views
from models import db, DB_NAME

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gbsdhagbfgjfda sdagusagsafigbsfagj'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')

    from models import User, Shelter

    with app.app_context():
        db.create_all()

    #create_database(app)

    return app

"""""
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
"""