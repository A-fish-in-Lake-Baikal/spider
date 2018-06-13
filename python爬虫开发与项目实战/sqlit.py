import sqlite3
import time

conn = sqlite3.connect('test.db')
c =conn.cursor()
datatime = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
# sql = '''CREATE TABLE `picture_url` (
# 	`picID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# 	`picurl`	TEXT,
# 	`datatime`	TEXT
# )'''
sql1 = 'insert into picture_url(picurl,datatime) values (?,?)'
sql2 = 'insert into page_url(pageurl,datatime) values(?,?)'
vla1 = ('https://wx1.sinaimg.cn/mw600/46401622gy1fra33m4gd1j20u00gwjrx.jpg',datatime)
vla2 = ('https://www.xitmi.com/1555.html',datatime)
# c.execute(sql)
c.execute(sql1,vla1)
c.execute(sql2,vla2)
print(datatime)
print('写入完成')
conn.commit()
conn.close()