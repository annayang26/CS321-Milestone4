# create the app and database
from venv import create
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path 
import os
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, login_required, UserMixin 
from dotenv import load_dotenv 

load_dotenv()
db = SQLAlchemy()
DB_NAME ="database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    db.init_app(app)
    migrate = Migrate(app, db)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    # create_database(app)

    loging_manager = LoginManager()
    loging_manager.login_view = 'auth.login'
    loging_manager.init_app(app)

    @loging_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
