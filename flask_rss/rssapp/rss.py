import sys
import urllib2
import HTMLParser
import xml.etree.ElementTree as ET
from logging import getLogger
class Rss(object):
    """A class for handling RSS feeds"""
    def __init__(self,url=None):
        if not url:
            self.url = ''
            self.articles = ''
        else:
            self.url = url
            self.articles = []
        self.logger = getLogger(__name__)
    def get_rss_into_articles(self):
        self.xml = urllib2.urlopen(self.url.encode('utf-8')).read()
        root = ET.fromstring(self.xml)
        for item in root.findall(".//item"):
            try:
                title = item.find("title")
                link = item.find("link")
                descr = item.find("description")
                pubDate = item.find("pubDate")
                strgDate = str(pubDate.text)
                article = Article(title.text,link.text,descr.text, strgDate)
                self.articles.append(article)
            except Exception as e:
                self.logger.error("Error in get_rss routine! Error report: " + e)
        return self.articles



class Article(object):
    """A class for handling the details of an article"""
    def __init__(self):
        self.title = ''
        self.link = ''
        self.descr = ''
        self.pubDate = ''
        self.pic_links = []
        self.logger = getLogger(__name__)

    def __init__(self, title,link,descr,pubDate):
        self.title = title
        self.link = link
        self.descr = descr
        self.pubDate = pubDate
        self.full_txt = ""
        self.pic_links = []
        self.pics = []

    def get_full_txt(self):
        try:
            response = urllib2.urlopen(self.link).read().decode('utf-8', 'ignore')
            parser = RssHTMLParser()
            parser.feed(response)
            self.pic_links = parser.img_links
            self.full_txt = parser.data
        except Exception as e:
            self.logger.error("Error in get_full_txt() of RssClass.Article Error: " + e)

    def get_photos(self, pic_links=None):
        pics = []
        if pic_links == None:
            try:
                for link in self.pic_links:
                    img = urllib2.urlopen(link).read()
                    #f = open('/home/parallels/Desktop/pic.jpg', 'wb')
                    #f.write(img)
                    #f.close()
                    self.pics.append(img)
            except Exception as e:
                self.logger.error("Error in RssClass.get_photos() using self.pic_links. Error: " + e)
        else:
            try:
                for link in pic_links:
                    image = urllib2.urlopen(self.link).read()
                    pics.append(image)
            except Exception as e:
                self.logger.error("Error in RssClass.get_photos() using pic_links. Error: " + e)
            return pics

class RssHTMLParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.is_start_p = False
        self.is_end_p = False
        self.is_start_sp = False
        self.data = ""
        self.img_links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.is_start_p = True
        elif tag == 'span':
            self.is_start_sp = True
        elif self.is_start_p and tag == 'a':
            self.is_start_p = True
        elif self.is_start_p and tag == 'img' or self.is_start_sp and tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.img_links.append(attr[1])
        else:
            self.is_start_p = False
            self.is_start_sp = False

    def handle_endtag(self, tag):
        if tag == 'p':
            self.is_start_p = False
            self.is_end_p = True
        elif tag == 'a' and self.is_start_p:
            self.is_start_p = True
        else:
            self.is_end_p = False

    def handle_data(self, data):
        if self.is_start_p:
            self.data += data
        elif self.is_end_p:
            self.data += ' '
        
