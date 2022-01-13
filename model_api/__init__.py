from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'\x82\x13\xd5\x06\x14z\xc7\xb5\xfc\x19\xbb\xf3\xbek\x11\xe6\xa9LT\xd6\xef\xec\xbd\x96'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    create_database(app)

    from .views import views
    app.register_blueprint(views)

    return app


def create_database(app):
    if not os.path.isfile(f'model_API/{DB_NAME}'):
        db.create_all(app=app)
