from datetime import datetime
from . import db
from flask_login import UserMixin


# User database model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    contactno = db.Column(db.Integer, index=True, nullable=False)
    address = db.Column(db.String(200), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    bids = db.relationship('Bids', backref='users')
    items = db.relationship('Item', backref='users')


# Item database model
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(400))
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    start_currency = db.Column(db.DECIMAL, precision=2, nullable=False)


    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    bids = db.relationship('Bids', backref='items')


    def __repr__(self):
        return "<Name: {}>".format(self.name)

# Bid database model


class Bids(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    bid_amount = db.Column(db.DECIMAL, precision=2, nullable=False)
    bid_date = db.Column(db.DateTime, default=datetime.now())

    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

# Login class
class Login:
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd
