import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome')
cursor = conn.cursor()
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

for info in feed_response:
    print info['content']['topic_title'].decode('unicode-escape')