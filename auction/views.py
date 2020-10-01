from flask import Blueprint, render_template, request, session
from .models import Login

mainbp = Blueprint('main', __name__)

email = "Login"
pwd = "pwd"
user = Login(email, pwd)

@mainbp.route('/')
def index():
    print(request.values.get('email'))
    print(request.values.get('pwd'))
    return render_template('index.html', user=user)


@mainbp.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user)


@mainbp.route('/mylistings')
def create():
    return render_template('mylistings.html', user=user)


@mainbp.route('/listings')
def listings():
    return render_template('listings.html', user=user)


@mainbp.route('/item')
def item():
    return render_template('item.html', user=user)


@mainbp.route('/login')
def login():
    if 'email' in session:
        return render_template('logout.html', user=user)
    else:
        return render_template('login.html', user=user)


@mainbp.route('/loginrequest', methods=['GET', 'POST'])
def loginreq():

    global user
    global email
    global pwd

    print(request.values.get('email'))
    email = request.values.get('email')
    print(request.values.get('pwd'))
    pwd = request.values.get('pwd')
    session['email'] = email
    user = Login(email, pwd)
    return index()


@mainbp.route('/logoutrequest', methods=['GET', 'POST'])
def logoutreq():
    if 'email' in session:
        session.pop('email', None)
    global user
    global email
    global pwd
    email = "Login"
    pwd = "pwd"
    user = Login(email, pwd)
    return render_template('index.html', user=user)

@mainbp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('index.html', user=user)