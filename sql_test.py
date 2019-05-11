# coding=utf-8
'''
author:马维畅
time：2019/5/10 14:42
'''

import pymssql
def sqlexecute():
    conn = pymssql.connect('192.168.2.142','sa','test12#$%','PSCR103')
    cursor = conn.cursor()

    sql = """select * from  PS_Resource"""

    cursor.execute(sql)
    for row in cursor:
        print(row)
    conn.commit()
    conn.close()

if __name__=='__main__':
    while True:
        sqlexecute()
