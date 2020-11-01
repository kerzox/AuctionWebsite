import flask
from flask import Blueprint, render_template, request, session, url_for, redirect, flash, Flask, abort
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
    user = current_user
    item = Item.query.filter_by(id=id).first()
    bid = db.session.query(db.func.max(Bids.bid_amount)).filter(Bids.items.has(id=id)).scalar()

    exists = db.session.query(Item.id).filter_by(id=id).scalar()
    if (exists == None):
        abort(404)

    bid_form = AddBidForm()
    return render_template('listing/item.html', item=item, bid=bid, bid_form=bid_form, user=user)


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
    user = current_user
    return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items, user=user)


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

@listingbp.route('/mylistings', methods=['GET', 'POST'])
@login_required
def mylistings():
    if flask.request.method == 'POST':
        remove_id = request.form.get("remove")
        if remove_id is not None:
            if 'remove' in remove_id:
                x = remove_id.split()
                print(x)
                item = Item.query.filter_by(id=x[0]).first()
                print(item)
                item.status = False
                db.session.commit()
                
            return redirect(url_for('listing.mylistings'))

        return redirect(url_for('listing.mylistings'))
    else:
        b_items = []
        namelist = []
        bid_id = []
        mylist = Item.query.filter_by(user_id=current_user.id).all()

        for item in mylist:
            b_items.append(Bids.query.filter(Bids.item_id==item.id).all())
            print(b_items)

        for bids in b_items:
            for b in bids:
                bid_id.append(b.item_id)
                name = User.query.filter_by(id=b.user_id).first()
                namelist.append(name.name)

        category_form = CategoryForm()
        print(namelist)
        return render_template('listing/mylistings.html', form=category_form, mylist=mylist, bid_id=bid_id, bidlist=b_items, username=namelist)



@listingbp.route('/search/category', methods=['GET', 'POST'])
def category():
    category_form = CategoryForm()
    bid_form = AddBidForm()
    user = current_user
    if category_form.validate_on_submit():
        cat = category_form.category.data
        if cat == 'None':
            items = Item.query.all()
            return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items, user=user)
        else:
            items = Item.query.filter(Item.category == cat).all()
            return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items, user=user)
    else:
        cat = request.form.get("search")
        if cat == 'All':
            items = Item.query.all()
            return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items, user=user)
        else:
            items = Item.query.filter(Item.category == cat).all()
            return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items=items, user=user)

@listingbp.route('/search')
def search():
    category_form = CategoryForm()
    bid_form = AddBidForm()
    user = current_user
    if request.args['search']:
        searchitem = "%" + request.args['search'] + '%'
        items = Item.query.filter(Item.name.like(searchitem)).all()
        return render_template('listing/listings.html', form=category_form, bid_form=bid_form, items = items, user=user)
    else:
        return redirect(url_for('listing.listings'))