<<<<<<< HEAD
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
=======
from . import db

class Item:
    def __init__(self, name, description, image, currency):
        self.name = name
        self.description = description
        self.image = image
        self.currency = currency
        self.comments = list()
    
    def set_comments(self, comment):
        self.comments.append(comment)


class Comment:
    def __init__(self, user, text, created_at):
        self.user = user
        self.text = text
        self.created_at = created_at
>>>>>>> c5cf62923cff0fcdc8c65f4d877580b4c1e08724
