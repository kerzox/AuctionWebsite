from flask import Blueprint, render_template, request, session, url_for, redirect
from .forms import CreateListingForm
from .models import Item

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    print(request.values.get('email'))
    print(request.values.get('pwd'))
    items = Item.query.all()
    return render_template('index.html', items=items)


@mainbp.route('/search')
def search():
    if request.args['search']:
        item = "%" + request.args['search'] + '%'
        items = Item.query.filter(
            Item.name.like(item)).all()
        return render_template('index.html', items=items)
    else:
        return redirect(url_for('main.index'))


@mainbp.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')
