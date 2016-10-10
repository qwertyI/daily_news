from sqlalchemy import Column, String, DateTime,create_engine, Integer, Text, INT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import settings

Base = declarative_base()


class Testerhome_Topic(Base):
    __tablename__ = 'topic'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    topic_title = Column(String(500))
    topic_href = Column(String(200))
    topic_author = Column(String(256))
    topic_author_img = Column(String(256))
    topic_class = Column(String(256))
    topic_reply_num = Column(Integer)
    spider_time = Column(String(256))

    def __init__(self, topic_title, topic_href, topic_author, topic_class, topic_reply_num, spider_time, topic_author_img):
        # self.topic_id = topic_id
        self.topic_title = topic_title
        self.topic_href = topic_href
        self.topic_author = topic_author
        self.topic_author_img = topic_author_img
        self.topic_class = topic_class
        self.topic_reply_num = topic_reply_num
        self.spider_time = spider_time

    def __repr__(self):
        return "<Topic(topic_title='%s', topic_author='%s', topic_class='%s', topic_reply_num='%s')>" % (
        self.topic_title, self.topic_author, self.topic_class, self.topic_reply_num)


class Topic_Detail(Base):
    __tablename__ = 'topic_detail'

    id = Column(INT, primary_key=True, unique=True, autoincrement=True)
    topic_id = Column(Integer)
    topic_title = Column(Text)
    topic_author = Column(String(256))
    topic_body = Column(Text)
    topic_like_num = Column(Integer)
    topic_reply_num = Column(Integer)
    topic_timeago = Column(String(256))
    spider_time = Column(String(256))

    def __init__(self, topic_id, topic_title, topic_author, topic_body, topic_reply_num, topic_timeago, topic_like_num, spider_time):
        self.topic_id = topic_id
        self.topic_title = topic_title
        self.topic_author = topic_author
        self.topic_body = topic_body
        self.topic_like_num = topic_like_num
        self.topic_reply_num = topic_reply_num
        self.topic_timeago = topic_timeago
        self.spider_time = spider_time


class CnBlogNews(Base):
    __tablename__ = 'cnblog'

    id = Column(INT, primary_key=True, unique=True, autoincrement=True)
    title = Column(String(500))
    recommended = Column(Integer)
    readed = Column(Integer)
    href = Column(String(200))

    def __init__(self, title, recommended, readed, href):
        self.title = title
        self.recommended = recommended
        self.readed = readed
        self.href = href

DBSession = sessionmaker(bind=settings.engine)
