from datetime import datetime
from . import db
from flask_login import UserMixin


# User database model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)


# Item database model
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3), nullable=False)

    def __repr__(self):
        return "<Name: {}>".format(self.name)


# Login class
class Login:
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd
