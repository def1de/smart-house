from flask import Flask
from .extentions import api, db
from .resources import ns


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    api.init_app(app)
    db.init_app(app)
    db.create_all()

    api.add_namespace(ns)

    return app