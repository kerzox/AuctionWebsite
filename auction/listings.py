from flask import Blueprint, render_template, request, session, url_for, redirect
from .forms import CreateListingForm
from .models import Item
from werkzeug.utils import secure_filename 
from . import db
import os

listingbp = Blueprint('listing', __name__, url_prefix='/listings')

@listingbp.route('/mylistings')
def mylistings():
    return render_template('listing/mylistings.html')

def check_upload_file(form):
    fp = form.image.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)

    upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
    db_upload_path='/static/image/' + secure_filename(filename)
    fp.save(upload_path)
    return db_upload_path

@listingbp.route('/create', methods = ['GET', 'POST'])
def create():
    create_form = CreateListingForm()
    if create_form.validate_on_submit():
        db_file_path = check_upload_file(create_form)
        listing = Item(name=create_form.title.data,
                       category=create_form.category.data,
                       description=create_form.description.data,
                       image=db_file_path,
                       start_currency=create_form.start_bid.data)
        print('Successfully created new listing', 'success')
        db.session.add(listing)
        db.session.commit()
        return redirect(url_for('listing.mylistings'))
    return render_template('listing/create.html', form=create_form)

@listingbp.route('/listings')
def listings():
    return render_template('listing/listings.html')

@listingbp.route('/item')
def item():
    return render_template('listing/item.html')
