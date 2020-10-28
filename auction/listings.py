from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from .forms import CreateListingForm, CategoryForm, AddBidForm
from .models import Item, Bids, User
from sqlalchemy import func
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from . import db
import os
import sqlite3

listingbp = Blueprint('listing', __name__, url_prefix='/listings')

@listingbp.route('/item/<id>')
def item(id):
    item = Item.query.filter_by(id=id).first()
    bid = db.session.query(db.func.max(Bids.bid_amount)).filter(Bids.items.has(id=id)).scalar()

    bid_form = AddBidForm()
    return render_template('listing/item.html', item=item, bid=bid, bid_form=bid_form)


def check_upload_file(form):
    fp = form.image.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)

    upload_path = os.path.join(
        BASE_PATH, 'static/image', secure_filename(filename))
    db_upload_path = '/static/image/' + secure_filename(filename)
    fp.save(upload_path)
    return db_upload_path


@listingbp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    create_form = CreateListingForm()
    if create_form.validate_on_submit():
        db_file_path = check_upload_file(create_form)
        listing = Item(name=create_form.title.data,
                       category=create_form.category.data,
                       description=create_form.description.data,
                       image=db_file_path,
                       start_currency=round(float(create_form.start_bid.data), 2),
                       curr_currency=round(float(create_form.start_bid.data), 2),
                       users=current_user)

        print('Listing has been created', 'success')
        db.session.add(listing)
        db.session.commit()
        return redirect(url_for('listing.mylistings'))
    return render_template('listing/create.html', form=create_form)


@listingbp.route('/listings')
def listings():
    items = Item.query.all()
    category_form = CategoryForm()
    bid_form = AddBidForm()
    return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items)


@listingbp.route('/<id>/bid', methods=['POST'])
@login_required
def bid(id):
    bid_form = AddBidForm()
    grab_item = Item.query.filter_by(id=id).first()
    grab_user = current_user
    if bid_form.validate_on_submit():

        new_bid = bid_form.bid_amount.data
        curr_bid = db.session.query(db.func.max(Bids.bid_amount)).filter(Bids.items.has(id=id)).scalar()
        print(new_bid, curr_bid)
        if (curr_bid == None):
            curr_bid = db.session.query(Item.start_currency).filter_by(id=id).scalar()
        if (new_bid > curr_bid):
            bid_commit = Bids(bid_amount=bid_form.bid_amount.data,
                              users=grab_user,
                              items=grab_item)
            db.session.add(bid_commit)
            update_currency = Item.query.get(id)
            update_currency.curr_currency = bid_form.bid_amount.data

            db.session.commit()
            print("Successfully added a new bid")
        else:
            error = ("Bid must be higher than the current highest bid!")
            flash(error, 'danger')
            return redirect(url_for('listing.item', id=id))
    return redirect(url_for('listing.item', id=id))

@listingbp.route('/mylistings')
@login_required
def mylistings():
    mylist = Item.query.filter_by(user_id=current_user.id).all()
    category_form = CategoryForm()
    return render_template('listing/mylistings.html', form=category_form, mylist=mylist)


@listingbp.route('/search', methods=['GET', 'POST'])
def search():
    category_form = CategoryForm()
    bid_form = AddBidForm()
    if category_form.validate_on_submit():
        cat = category_form.category.data
        if cat == 'None':
            items = Item.query.all()
            return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items)
        else:
            items = Item.query.filter(Item.category == cat).all()
            return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items)
    else:
        cat = request.form.get("search")
        if cat == 'All':
            items = Item.query.all()
            return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items)
        else:
            items = Item.query.filter(Item.category == cat).all()
            return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items)
