from app import app
import requests
from flask import render_template
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome')
cursor = conn.cursor()


@app.route('/info')
def info():
    cursor.execute('select id, topic_title, topic_href, topic_reply_num from topic order by spider_time desc limit 10;')
    result = cursor.fetchone()
    feed_response = []
    while result is not None:
        response = {'id': result[0], 'content': {}}
        response['content']['topic_title'] = result[1]
        response['content']['topic_href'] = result[2]
        response['content']['topic_reply_num'] = result[3]
        feed_response.append(response)
        result = cursor.fetchone()

    infos = []
    for response in feed_response:
        info = {}
        info['title'] = response['content']['topic_title'].decode('unicode-escape')
        info['href'] = response['content']['topic_href'].decode('unicode-escape')
        info['recommended'] = response['content']['topic_reply_num']
        info['readed'] = 0
        infos.append(info)

    class_status = ['current_nav', '']

    return render_template('main.html', infos=infos, class_status=class_status)


@app.route('/cnblog')
def cnblog():
    cursor.execute('select id, title, recommended, readed, href from cnblog order by spider_time desc limit 10;')
    result = cursor.fetchone()
    feed_response = []
    while result is not None:
        response = {'id': result[0], 'content': {}}
        response['content']['title'] = result[1]
        response['content']['recommended'] = result[2]
        response['content']['readed'] = result[3]
        response['content']['href'] = result[4]
        feed_response.append(response)
        result = cursor.fetchone()

    infos = []
    for response in feed_response:
        info = {}
        info['title'] = response['content']['title'].decode('unicode-escape')
        info['recommended'] = response['content']['recommended']
        info['readed'] = response['content']['readed']
        info['href'] = response['content']['href'].decode('unicode-escape')
        infos.append(info)

    class_status = ['', 'current_nav']

    return render_template('main.html', infos=infos, class_status=class_status)



