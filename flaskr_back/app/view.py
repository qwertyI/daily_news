from flask_restful import Resource, Api
from app import app
import MySQLdb


api = Api(app)


class Info(Resource):

    def get(self):
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            'select distinct(topic_href), topic_title, id, topic_href, topic_reply_num from topic order by spider_time desc limit 10;')
        result = cursor.fetchone()
        feed_response = []
        while result is not None:
            response = {'id': result[2], 'content': {}}
            response['content']['topic_title'] = result[1]
            response['content']['topic_href'] = result[3]
            response['content']['topic_reply_num'] = result[4]
            feed_response.append(response)
            result = cursor.fetchone()
        return feed_response


class CnBlog(Resource):

    def get(self):
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            'select distinct(href), title, id, recommended, readed, href from cnblog order by spider_time desc limit 10;')
        result = cursor.fetchone()
        feed_response = []
        while result is not None:
            response = {'id': result[2], 'content': {}}
            response['content']['title'] = result[1]
            response['content']['recommended'] = result[3]
            response['content']['readed'] = result[4]
            response['content']['href'] = result[5]
            feed_response.append(response)
            result = cursor.fetchone()
        return feed_response


class Bole(Resource):

    def get(self):
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')
        cursor = conn.cursor()
        cursor.execute('select distinct(href), title, id, img, href from bole order by id desc limit 10;')
        result = cursor.fetchone()
        feed_response = []
        while result is not None:
            response = {'id': result[2], 'content': {}}
            response['content']['title'] = result[1]
            response['content']['img'] = result[3]
            response['content']['href'] = result[4]
            feed_response.append(response)
            result = cursor.fetchone()
        return feed_response

api.add_resource(Info, '/info')
api.add_resource(CnBlog, '/cnblog')
api.add_resource(Bole, '/bole')

