from flask import Flask
from views import views
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin
from sqlalchemy.sql import func

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')

    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        biological_sex = db.Column(db.String(3), unique=False)
        has_children = db.Column(db.Boolean, unique=False, default=False)
        physical_disability = db.Column(db.Boolean, unique=False, default=False)
        mental_disability = db.Column(db.Boolean, unique=False, default=False)

    return app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True, port=8000)