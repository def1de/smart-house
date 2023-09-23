from flask import Flask
from .extentions import api, db
from .resources import ns
from .web.routes import web


def create_app():
    app = Flask(__name__)
    app.register_blueprint(web, url_prefix="/")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    return app