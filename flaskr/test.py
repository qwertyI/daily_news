import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', db='testerhome', charset='utf8')
cursor = conn.cursor()
cursor.execute('select * from topic order by id desc')
print cursor.fetchone()
cursor.execute('delete from topic where id = 217')
cursor.execute('select * from topic order by id desc')
print cursor.fetchone()

cursor1 = conn.cursor()
cursor1.execute('select * from topic order by id desc')
print cursor1.fetchone()