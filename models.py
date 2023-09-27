from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()
DB_NAME = "database.db"

class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        biological_sex = db.Column(db.String(3), unique=False)
        has_children = db.Column(db.Boolean, unique=False, default=False)
        physical_disability = db.Column(db.Boolean, unique=False, default=False)
        mental_disability = db.Column(db.Boolean, unique=False, default=False)