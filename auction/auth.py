from flask import Blueprint, session, redirect, url_for, render_template
from .forms import LoginForm, RegisterForm

authentication_blueprint = Blueprint('authentication', __name__, url_prefix='/authentication')

#Login Blueprint
@authentication_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        session['email'] = login_form.email.data
        return redirect(url_for('authentication.login'))

    return render_template('authentication/login.html', form=login_form)

#Register Blueprint
@authentication_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        return redirect(url_for('authentication.login'))

    return render_template('authentication/register.html', form=register_form)

#Logout Blueprint
@authentication_blueprint.route('/logout')
def logout():
    print(session)
    session.clear()
    return render_template('authentication/logout.html')