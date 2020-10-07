from flask import Blueprint, render_template, request, session, url_for, redirect
from .forms import CreateListingForm

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    print(request.values.get('email'))
    print(request.values.get('pwd'))
    return render_template('index.html')

@mainbp.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')