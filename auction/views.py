from flask import Blueprint, render_template, request, session

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    print(request.values.get('email'))
    print(request.values.get('pwd'))
    return render_template('index.html')


@mainbp.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')


@mainbp.route('/mylistings')
def create():
    return render_template('mylistings.html')


@mainbp.route('/listings')
def listings():
    return render_template('listings.html')


@mainbp.route('/item')
def item():
    return render_template('item.html')
