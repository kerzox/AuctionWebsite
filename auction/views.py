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


@mainbp.route('/mylistings')
def mylistings():

    return render_template('mylistings.html')

@mainbp.route('/create', methods = ['GET', 'POST'])
def create():

    create_form = CreateListingForm()
    if create_form.validate_on_submit():
        print('form is valid')
        return redirect('mylistings')
    else:
        print("form is not valid")
    return render_template('create.html', form=create_form)
    


@mainbp.route('/listings')
def listings():
    return render_template('listings.html')


@mainbp.route('/item')
def item():
    return render_template('item.html')
