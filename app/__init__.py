from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "not so secret key"
    from .bgmysql import cnx, sql_exec, mydbhost, mydbname, mydbpass, mydbuser

    # MySQL

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{mydbuser}:{mydbpass}@{mydbhost}/{mydbname}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    cur = cnx.cursor()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.signin'
    login_manager.login_message = ''
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
