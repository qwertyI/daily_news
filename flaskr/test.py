import requests
import json
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')
cursor = conn.cursor()
cursor.execute('update topic set topic_title = \'222222\' where topic_href=\'https://testerhome.com//topics/6103\';')
print len(cursor.fetchall())
