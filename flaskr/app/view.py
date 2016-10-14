# -*- coding: utf-8 -*-
from app import app, server_url
import requests
from flask import render_template, redirect, url_for
import json


@app.route('/')
def index():
    return redirect(url_for('info'))


@app.route('/info')
def info():
    feed_response = json.loads(requests.get(server_url + '/info').content)

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
    feed_response = json.loads(requests.get(server_url + '/cnblog').content)

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
    feed_response = json.loads(requests.get(server_url + '/bole').content)

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



