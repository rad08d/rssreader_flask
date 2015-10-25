__author__ = 'alan'
import flask_rss.customlogg
from flask import Blueprint

rssapp_blueprint = Blueprint('rssapp', __name__)

from . import views