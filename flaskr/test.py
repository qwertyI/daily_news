import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')
cursor = conn.cursor()
cursor.execute('select distinct(topic_href), topic_title, id, topic_href, topic_reply_num from topic order by spider_time desc limit 10;')
result = cursor.fetchall()

print result[6]
print result[8]
print result[6][0] == result[8][0]