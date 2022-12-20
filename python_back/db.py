import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', database='test', port=3306, charset='utf8')

curs = conn.cursor()

# curs.execute('CREATE TABLE userTable (id char(4), userName char(15), email char(20), birthYear int)')

curs.execute("INSERT INTO userTable VALUES ('test', 'test', 'test', 1990)")
curs.execute("INSERT INTO userTable VALUES ('test', 'test2', 'test2', 1981)")

conn.commit()
conn.close()