__author__ = 'alan'
from . import rssapp_blueprint
from flask import render_template
from os import path
from logging import getLogger
from flask_rss import customlogg
from settings import Configuration
import rss

logger = getLogger(__name__)
config = Configuration()

@rssapp_blueprint.route('/')
def index():
    try:
        dirname = path.dirname(__file__)
        sitespath = path.join(dirname, config.RSSWEBSITES)
        file = open(sitespath)
        sites = file.readlines()
        sitestories = []
        group = 0
        for site in sites:
            try:
                rsslink = rss.Rss(site)
                rsslink.get_rss_into_articles()
                articlegrouping = {group: rsslink}
                sitestories.append(articlegrouping)
                group += 1
            except Exception as e:
                logger.error("There has been an error in the index method. Error: " + str(e))
    except Exception as e:
        #logger.error("There has been an error in the index method. Error: " + str(e))
        print e
    return render_template('index.html', stories=sitestories)