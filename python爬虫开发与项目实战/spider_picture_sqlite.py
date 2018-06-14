from urllib import request,error
import re
import ssl
import os
import sqlite3
import time

def getlink(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    ssl._create_default_https_context = ssl._create_unverified_context
    file = request.Request(url,headers=headers)
    page = request.urlopen(file)
    data = str(page.read())
    pat = '(https?://[^\s)";]+\.(\w|/)+.html)'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link
def getpic(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    ssl._create_default_https_context = ssl._create_unverified_context
    file1 = request.Request(link,headers=headers)
    page1 = request.urlopen(file1)
    data1 = str(page1.read())
    pattern = '(https?://[^\s)";]+\.(\w|/)+(.jpg|.png|.gif))'
    piclinks = re.compile(pattern).findall(data1)
    piclinks = list(set(piclinks))
    return piclinks

if __name__=='__main__':
    print('开始爬行~~')
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    datatime = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    urls = ['https://www.xitmi.com/tag/fuli/page{}'.format(str(i)) for i in range(1,6)]
    path = os.path.abspath('.')
    x = 1
    for url in urls:
        try:
            linklist = getlink(url)
            for link in linklist:

                with open(path+"//status.txt","a") as file:
                    file.write(link[0]+'\n')
                # print(link[0])
                try:
                    piclink = getpic(link[0])
                except error.URLError as e:
                    # print(e.code)
                    print(e.reason)
                y = 1
                for p in piclink:
                    sql1 = 'insert into picture_url(picurl,datatime,fatherid) values (?,?,?)'
                    vla1 = (p[0], datatime,x)
                    c.execute(sql1, vla1)
                    with open(path + "//status.txt", "a") as file:
                        file.write('\t'+'第%s个网页,第%s次爬取.链接为：%s' %(x,y,p[0])+ '\n')
                    print('第%s个网页,第%s次爬取.链接为：%s' %(x,y,p[0]))
                    y += 1
                    # print(p[0])
                x += 1
                sql2 = 'insert into page_url(pageurl,datatime,count) values(?,?,?)'
                vla2 = (link[0], datatime,y)
                c.execute(sql2, vla2)
        except error.URLError as e:
            # print(e.code)
            print(e.reason)
    print('爬行结束~~')
    conn.commit()
    conn.close()