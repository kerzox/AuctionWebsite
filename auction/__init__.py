import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db=SQLAlchemy()

def create_app():
    print(__name__)
    app = Flask(__name__)
    app.secret_key = 'Secret'

    #set the app configuration data 
    app.config[SQLALCHEMY_DATABASE_URI]= os.environ['DATABASE_URL']
    #initialize postgres
    db.init_app(app)

    bootstrap = Bootstrap(app)

    from . import views
    app.register_blueprint(views.mainbp)

    from . import items
    app.register_blueprint(items.bp)

    from .auth import authentication_blueprint
    app.register_blueprint(authentication_blueprint)

    return app
