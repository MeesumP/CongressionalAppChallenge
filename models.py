from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        biological_sex = db.Column(db.String(5), unique=False)
        has_children = db.Column(db.Boolean, unique=False, default=False)
        has_disability = db.Column(db.Boolean, unique=False, default=False)

class Shelter(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(10000), unique=True)
        agency = db.Column(db.String(1000), unique=True)
        location = db.Column(db.String(1000), unique=True)
        description = db.Column(db.String(10000000), unique=True)
        supports_families = db.Column(db.Boolean, unique=False, default=False)
        supports_gender = db.Column(db.String(25), unique=False, default="Both Sexes")
        supports_disabilities = db.Column(db.Boolean, unique=False, default=False)

class Ticket(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(1000), unique=False)
        info = db.Column(db.String(10000000000000), unique=False)