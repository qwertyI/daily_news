# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TesterhomeSpiderItem(scrapy.Item):
    topic_title = scrapy.Field()
    topic_href = scrapy.Field()
    topic_author = scrapy.Field()
    topic_author_img = scrapy.Field()
    topic_class = scrapy.Field()
    topic_reply_num = scrapy.Field()


class CnBlogSpiderItem(scrapy.Item):
    title = scrapy.Field()
    recommended = scrapy.Field()
    readed = scrapy.Field()
    href = scrapy.Field()


class BoleSpiderItem(scrapy.Item):
    title = scrapy.Field()
    img = scrapy.Field()
    href = scrapy.Field()

