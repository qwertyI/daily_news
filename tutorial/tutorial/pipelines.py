# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from testerhome_db import Testerhome_Topic, DBSession, Topic_Detail, CnBlogNews
from scrapy.log import logger
import settings
import functools
import sys, datetime

reload(sys)
sys.setdefaultencoding('utf-8')


def check_spider_pipeline(process_item_method):
    """该注解用在pipeline上

    :param process_item_method:
    :return:
    """

    @functools.wraps(process_item_method)
    def wrapper(self, item, spider):

        # message template for debugging
        msg = " {0} pipeline step".format(self.__class__.__name__)

        # if class is in the spider"s pipeline, then use the
        # process_item method normally.
        if self.__class__ in spider.pipeline:
            logger.info(msg.format("executing"))
            return process_item_method(self, item, spider)

        # otherwise, just return the untouched item (skip this step in
        # the pipeline)
        else:
            logger.info(msg.format("skipping"))
            return item

    return wrapper


class TesterhomeSpiderPipeline(object):

    def __init__(self):
        self.session = DBSession()

    @check_spider_pipeline
    def process_item(self, item, spider):
        my_topic = Testerhome_Topic(topic_title=item['topic_title'][0].encode('unicode-escape').decode('unicode-escape'),
                                    topic_href=item['topic_href'][0].encode('unicode-escape').decode('unicode-escape'),
                                    topic_author=item['topic_author'][0].encode('unicode-escape').decode('unicode-escape'),
                                    topic_author_img=item['topic_author_img'][0].encode('unicode-escape').decode('unicode-escape'),
                                    topic_class=item['topic_class'][0].encode('unicode-escape').decode('unicode-escape'),
                                    topic_reply_num=item['topic_reply_num'][0].encode('unicode-escape').decode('unicode-escape'),
                                    spider_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').decode('unicode-escape'))
        try:
            self.session.add(my_topic)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()
        return item


class CnBlogSpiderPipeline(object):

    def __init__(self):
        self.session = DBSession()

    @check_spider_pipeline
    def process_item(self, item, spider):
        cn_blog_news = CnBlogNews(title=item['title'][0].encode('unicode-escape').decode('unicode-escape'),
                                  recommended=item['recommended'][0].encode('unicode-escape').decode('unicode-escape'),
                                  href=item['href'][0].encode('unicode-escape').decode('unicode-escape'),
                                  readed=item['readed'][0].encode('unicode-escape').decode('unicode-escape'))
        try:
            self.session.add(cn_blog_news)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()
        return item
