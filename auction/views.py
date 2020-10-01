from flask import Blueprint, render_template, request, session
from .models import Login

mainbp = Blueprint('main', __name__)

email = "Login"
pwd = "pwd"
user = Login(email, pwd)

@mainbp.route('/')
def index():
    print(request.values.get('email'))
    print(request.values.get('pwd'))
    return render_template('index.html', user=user)


@mainbp.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user)


@mainbp.route('/mylistings')
def create():
    return render_template('mylistings.html', user=user)


@mainbp.route('/listings')
def listings():
    return render_template('listings.html', user=user)


@mainbp.route('/item')
def item():
    return render_template('item.html', user=user)
