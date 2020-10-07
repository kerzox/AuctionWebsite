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
    # Relationships
    bids = db.relationship('Bids', backref='user')


# Item database model
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(400))
    category = db.Column(db.String(50), nullable=False)
    start_currency = db.Column(db.DECIMAL, nullable=False)
    # Relationships
    bids = db.relationship('Bids', backref='item')

    def __repr__(self):
        return "<Name: {}>".format(self.name)

# Bid database model
class Bids(db.Model):
    __tablename__= 'bids'
    id = db.Column(db.Integer, primary_key=True)
    bid_amount = db.Column(db.DECIMAL, nullable=False)
    bid_date = db.Column(db.DateTime, nullable=False)
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))


# Login class
class Login:
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd