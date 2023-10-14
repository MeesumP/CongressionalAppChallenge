from flask import Flask
from views import views
from contact import contact
from search import search
from admin import admin
from models import db, DB_NAME

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gbsdhagbfgjfda sdagusagsafigbsfagj'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(contact, url_prefix='/contact')
    app.register_blueprint(search, url_prefix='/search')
    app.register_blueprint(admin, url_prefix='/admin')

    from models import User, Ticket

    with app.app_context():
        db.create_all()

    return app