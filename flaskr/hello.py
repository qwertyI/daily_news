from flask import Flask
from flask_restful import Resource, Api
import MySQLdb
from app import app

api = Api(app)

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome')
cursor = conn.cursor()


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


class test_newest_info(Resource):

    def get(self):
        cursor.execute('select id, topic_title, topic_href, topic_author from topic order by id desc limit 10;')
        result = cursor.fetchone()
        feed_response = []
        while result is not None:
            response = {'id': result[0], 'content': {}}
            response['content']['topic_title'] = result[1]
            response['content']['topic_href'] = result[2]
            response['content']['topic_author'] = result[3]
            feed_response.append(response)
            result = cursor.fetchone()
        return feed_response

api.add_resource(HelloWorld, '/')
api.add_resource(test_newest_info, '/test_newest_info')

if __name__ == '__main__':
    app.run(debug=True)
