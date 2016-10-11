# -*- coding: utf-8 -*-
from app import app
import requests
from flask import render_template
import MySQLdb


@app.route('/')
@app.route('/info')
def info():
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select distinct(topic_href), topic_title, id, topic_href, topic_reply_num from topic order by spider_time desc limit 10;')
    result = cursor.fetchone()
    feed_response = []
    while result is not None:
        response = {'id': result[2], 'content': {}}
        response['content']['topic_title'] = result[1]
        response['content']['topic_href'] = result[3]
        response['content']['topic_reply_num'] = result[4]
        feed_response.append(response)
        result = cursor.fetchone()

    infos = []
    for response in feed_response:
        info = {}
        info['id'] = response['id']
        info['title'] = response['content']['topic_title']
        info['href'] = response['content']['topic_href']
        info['recommended'] = response['content']['topic_reply_num']
        info['readed'] = 0
        infos.append(info)

    class_status = ['current_nav', '']

    return render_template('main.html', infos=infos, class_status=class_status)


@app.route('/cnblog')
def cnblog():
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select distinct(href), title, id, recommended, readed, href from cnblog order by spider_time desc limit 10;')
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

    infos = []
    for response in feed_response:
        info = {}
        info['id'] = response['id']
        info['title'] = response['content']['title']
        info['recommended'] = response['content']['recommended']
        info['readed'] = response['content']['readed']
        info['href'] = response['content']['href']
        infos.append(info)

    class_status = ['', 'current_nav']

    return render_template('main.html', infos=infos, class_status=class_status)



