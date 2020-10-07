from flask import Blueprint, render_template, request, session, url_for, redirect
from .forms import CreateListingForm

listingbp = Blueprint('listing', __name__, url_prefix='/listings')

@listingbp.route('/mylistings')
def mylistings():
    return render_template('listing/mylistings.html')

@listingbp.route('/create', methods = ['GET', 'POST'])
def create():

    create_form = CreateListingForm()
    if create_form.validate_on_submit():
        print('form is valid')
        return redirect('listings.mylistings')
    else:
        print("form is not valid")
    return render_template('listing/create.html', form=create_form)

@listingbp.route('/listings')
def listings():
    return render_template('listing/listings.html')

@listingbp.route('/item')
def item():
    return render_template('listing/item.html')
