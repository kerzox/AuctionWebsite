from flask import Blueprint, session, redirect, url_for, render_template, flash
from .forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required
from .models import User

authentication_blueprint = Blueprint('authentication', __name__, url_prefix='/authentication')

#Login Blueprint
@authentication_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if login_form.validate_on_submit():
        # grab all data from form
        username = login_form.user_name.data
        pwd = login_form.password.data
        # attempt to grab existing user
        u = User.query.filter_by(name=username).first()
        if u is None:
            error="Incorrect username or password."
        # if exists, compare passwords
        elif not check_password_hash(u.password_hash, pwd):
            error="Incorrect username or password."
        # if match, login
        if error is None:
            # if error is none, success
            login_user(u)
            session['email'] = login_form.user_name.data
            return redirect(url_for('main.index'))
        else:
            flash(error, 'danger')
            return redirect(url_for('authentication.login'))
    return render_template('authentication/login.html', form=login_form)

#Register Blueprint
@authentication_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        # grab all data from form
        username = register_form.user_name.data
        email = register_form.email_id.data
        pwd = register_form.password.data
        # check if username already exists
        u = User.query.filter_by(name=username).first() # returns user object or NONE
        if u:
            flash('This username already exists', 'danger')
            return redirect(url_for('authentication.register', form=register_form))
        # if username unique, create new user
        pwd_hash = generate_password_hash(pwd)
        new_user = User(name=username, emailid=email, password_hash=pwd_hash)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.index'))
    else:
        return render_template('authentication/register.html', form=register_form)

#Logout Blueprint
@authentication_blueprint.route('/logout')
def logout():
    print(session)
    logout_user()
    session.clear()
    return render_template('authentication/logout.html')