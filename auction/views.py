from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import Item, Login

mainbp = Blueprint('main', __name__)

email = "Login"
pwd = "pwd"
user = Login(email, pwd)


@mainbp.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)


@mainbp.route('/search')
def search():
    if request.args['search']:
        it = "%" + request.args['search'] + '%'
        items = Item.query.filter(Item.name.like(it)).all()
        return render_template('index.html', items=items)

    return redirect(url_for('main.index'))


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
