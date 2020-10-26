from flask import Blueprint, render_template, request, session, url_for, redirect
from .forms import CreateListingForm
from .models import Item, Bids
from sqlalchemy import func
from . import db

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    print(request.values.get('email'))
    print(request.values.get('pwd'))
    items = Item.query.order_by(Item.id.desc()).limit(6).all()

    apple = Item.query.filter(Item.category == "Apple").count()

    return render_template('index.html', items=items, apple = apple)


@mainbp.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')
