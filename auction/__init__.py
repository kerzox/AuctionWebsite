from flask import Flask

def create_app():
    print(__name__)
    app = Flask(__name__)
    app.secret_key = 'Secret'

    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI']='DATABASE_URL'

    from . import views
    app.register_blueprint(views.mainbp)

    from . import destinations
    app.register_blueprint(destinations.bp)

    return app