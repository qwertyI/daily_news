from app import app
import requests
from flask import render_template
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome')
cursor = conn.cursor()

@app.route('/info')
def info():
    cursor.execute('select id, topic_title, topic_href, topic_author, topic_author_img from topic order by id desc limit 10;')
    result = cursor.fetchone()
    feed_response = []
    while result is not None:
        response = {'id': result[0], 'content': {}}
        response['content']['topic_title'] = result[1]
        response['content']['topic_href'] = result[2]
        response['content']['topic_author'] = result[3]
        response['content']['topic_author_img'] = result[4]
        feed_response.append(response)
        result = cursor.fetchone()

    infos = []
    for response in feed_response:
        info = {}
        info['topic_title'] = response['content']['topic_title'].decode('unicode-escape')
        info['topic_href'] = response['content']['topic_href'].decode('unicode-escape')
        info['topic_author'] = response['content']['topic_author'].decode('unicode-escape')
        info['topic_author_img'] = response['content']['topic_author_img'].decode('unicode-escape')
        infos.append(info)

    return render_template('main.html', infos=infos)

