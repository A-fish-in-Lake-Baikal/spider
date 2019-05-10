# coding=utf-8
'''
author:马维畅
time：2019/5/10 14:42
'''

import pymssql
def sqlexecute():
    conn = pymssql.connect('192.168.2.142','sa','test12#$%','PSCR103')
    cursor = conn.cursor()

    sql = """select top 100 mf.ResourceID, sf.UniqueID, mf.FileID, mf.Path from 
                    (select R.ID as ResourceID, F.UniqueID, F.ID as FileID, F.Path
                        from
                        PS_Resource R
                        inner join PS_CategoryResource CR on CR.ResourceID = R.ID and R.IsDeleted = 0
                        inner join PS_ResourceFile RF on RF.ResourceID = R.ID or R.ParentResourceID =R.ID
                        inner join PS_File F on F.ID = RF.FileID and F.IsDeleted = 0
                        where
                        R.ResourceType = 3 and R.IsDeleted = 0 and RF.FileType = 1
                        and f.ID not in (select FileID from ImageAnalysisFace)) mf
                        join 
                        PS_ResourceFile rf on mf.FileID = rf.ParentFileID and rf.FileType=4
                        join 
                        PS_File sf on rf.FileID=sf.ID"""

    cursor.execute(sql)
    for row in cursor:
        print(row)
    conn.commit()
    conn.close()

if __name__=='__main__':
    while True:
        sqlexecute()