from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    print(__name__)
    app = Flask(__name__)
    app.secret_key = 'Secret'

    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI']='DATABASE_URL'
    #initialize postgres
    db.init_app(app)

    from . import views
    app.register_blueprint(views.mainbp)

    from . import items
    app.register_blueprint(items.bp)

    return app
