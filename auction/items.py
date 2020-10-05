from flask import Blueprint, render_template, request, session
from .models import Item

# create a blueprint
bp = Blueprint('item', __name__, url_prefix='/items')


@bp.route('/<id>')
def show(id):
    item = Item.query.filter_by(id=id).first()
    return render_template('items/show.html', item=item)


##############   USE THIS CODE LATER ######################
def get_item():
    # creating the description of Brazil
    b_desc = """Brazil is considered an advanced emerging economy.
   It has the ninth largest GDP in the world by nominal, and eight by PPP measures. 
   It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""
    # an image location
    image_loc = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
    item = Item('Brazil', b_desc, image_loc, '10 R$')
    return item
