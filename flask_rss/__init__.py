__author__ = 'alan'
from flask import Flask
from . import customlogg
from .rssapp import rssapp_blueprint
from .rssapp import rss

def create_app(config):
    app = Flask(__name__)
    add_blueprints(app)
    return app


def add_blueprints(app):
    app.register_blueprint(rssapp_blueprint)