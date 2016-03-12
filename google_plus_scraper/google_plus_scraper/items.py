# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from google_plus_scraper_app.models import GooglePlusArticle

class GooglePlusArticleItem(DjangoItem):
    django_model = GooglePlusArticle
