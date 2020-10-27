import flask
from flask import Blueprint, render_template, request, session, url_for, redirect
from flask_login import login_required, current_user
from .models import Item, Bids, Watchlist
from sqlalchemy import func
from . import db

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    print(request.values.get('email'))
    print(request.values.get('pwd'))
    items = Item.query.order_by(Item.id.desc()).limit(6).all()

    apple = Item.query.filter(Item.category == "Apple").count()
    google = Item.query.filter(Item.category == "Google").count()
    samsung = Item.query.filter(Item.category == "Samsung").count()
    sony = Item.query.filter(Item.category == "Sony").count()
    oppo = Item.query.filter(Item.category == "Oppo").count()
    allItems = Item.query.all()

    return render_template('index.html', items=items, apple = apple, 
                            google = google, samsung = samsung, sony = sony,
                            oppo = oppo, allItems = allItems)


@mainbp.route('/watchlist', methods=['GET', 'POST'])
@login_required
def watchlist():
    grab_user = current_user

    if flask.request.method == 'POST':
        remove_id = request.form.get("remove")
        add_id = request.form.get("watchlist")
        if remove_id is not None:
            if 'remove' in remove_id:
                x = remove_id.split()
                db.session.query(Watchlist.user_id).filter_by(item_id=x[0]).delete()
                db.session.commit()
                return redirect(url_for('main.watchlist'))

        submit_item = Item.query.filter_by(id=add_id).first()
        add_to_watchlist = Watchlist(items=submit_item,
                                     users=grab_user)
        db.session.add(add_to_watchlist)
        db.session.commit()
        print("added listing to watchlist")
        return redirect(url_for('main.watchlist'))
    else:
        watchlist_items = []
        for item in db.session.query(Watchlist.item_id).filter_by(user_id=current_user.id).all():
            watchlist_items.append(item.item_id)
        item_filter = db.session.query(Item).filter(Item.id.in_(watchlist_items)).all()

        return render_template('watchlist.html', items=item_filter)