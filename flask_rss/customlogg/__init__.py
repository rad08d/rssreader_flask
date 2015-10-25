__author__ = 'alandinneen'
from logging import basicConfig, DEBUG
from os import path

dirName = path.dirname(__file__)
logpath = path.join(dirName, "rsswebsite.log")
basicConfig(filename=logpath, filemode='w', level=DEBUG)