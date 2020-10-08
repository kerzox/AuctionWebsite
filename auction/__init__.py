import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db=SQLAlchemy()

def create_app():
    print(__name__)
    app = Flask(__name__)
    app.secret_key = 'Secret'
    
    # Heroku postgresql
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    # Will's local postgresql
    #app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pappin78w@localhost:5432/postgres"

    #initialize postgres
    db.init_app(app)

    bootstrap = Bootstrap(app)

    login_manager = LoginManager()
    login_manager.login_view = 'authentication.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from . import views
    app.register_blueprint(views.mainbp)

    from . import listings
    app.register_blueprint(listings.listingbp)

    from .auth import authentication_blueprint
    app.register_blueprint(authentication_blueprint)

    return app
