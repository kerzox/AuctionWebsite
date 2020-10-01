from flask import Blueprint, render_template, request, session
from .models import Item, Comment 

# create a blueprint
bp = Blueprint('item', __name__, url_prefix = '/items')


@bp.route('/<id>')
def show(id):
    item = get_item()
    return render_template('items/show.html', item = item)

##############   USE THIS CODE LATER ######################
def get_item():
  #creating the description of Brazil
  b_desc= """Brazil is considered an advanced emerging economy.
   It has the ninth largest GDP in the world by nominal, and eight by PPP measures. 
   It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""
  # an image location
  image_loc='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
  item = Item('Brazil',b_desc,image_loc,'10 R$')
  # a comment
  comment = Comment("User1", "Visited during the olympics, was great",'2019-11-12 11:00:00')
  comment2 = Comment("User2", "Visited during the olympics, was on",'2012-11-12 11:00:00')
  item.set_comments(comment)
  item.set_comments(comment2)
  return item