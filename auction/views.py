<<<<<<< HEAD
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
=======
from flask import Blueprint, render_template, request, session

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    print(request.values.get('email'))
    print(request.values.get('pwd'))
    return render_template('index.html')
>>>>>>> c5cf62923cff0fcdc8c65f4d877580b4c1e08724


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
