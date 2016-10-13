# -*- coding: utf-8 -*-
from app import app
import requests
from flask import render_template
import MySQLdb
import json

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')


@app.route('/')
@app.route('/info')
def info():
    feed_response = json.loads(requests.get('http://127.0.0.1:5001/info').content)

    infos = []
    for response in feed_response:
        info = {}
        info['id'] = response['id']
        info['title'] = response['content']['topic_title']
        info['href'] = response['content']['topic_href']
        info['recommended'] = response['content']['topic_reply_num']
        info['readed'] = 0
        infos.append(info)

    class_status = 'info'

    return render_template('main.html', infos=infos, class_status=class_status)


@app.route('/cnblog')
def cnblog():
    feed_response = json.loads(requests.get('http://127.0.0.1:5001/cnblog').content)

    infos = []
    for response in feed_response:
        info = {}
        info['id'] = response['id']
        info['title'] = response['content']['title']
        info['recommended'] = response['content']['recommended']
        info['readed'] = response['content']['readed']
        info['href'] = response['content']['href']
        infos.append(info)

    class_status = 'cnblog'

    return render_template('main.html', infos=infos, class_status=class_status)


@app.route('/bole')
def bole():
    # conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')
    feed_response = json.loads(requests.get('http://127.0.0.1:5001/bole').content)

    infos = []
    for response in feed_response:
        info = {}
        info['id'] = response['id']
        info['title'] = response['content']['title']
        info['recommended'] = 0
        info['readed'] = 0
        info['href'] = response['content']['href']
        infos.append(info)

    class_status = 'bole'

    return render_template('main.html', infos=infos, class_status=class_status)



