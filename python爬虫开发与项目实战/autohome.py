from urllib import request
from bs4 import BeautifulSoup
import sqlite3
import re

urls = ['https://www.autohome.com.cn/news/{}/#liststart'.format(str(i)) for i in range(1,4)]
x = 1
for url in urls:
    print('第%s頁' %x)
    # url = 'https://www.autohome.com.cn/news/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    # 添加头信息
    file = request.Request(url,headers=headers)
    # 读取网页内容
    page = request.urlopen(file).read().decode('gbk')
    soup = BeautifulSoup(page,'html.parser')
    li_list = soup.find(id='auto-channel-lazyload-article').find_all('li')
    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    for li in li_list:
        title = li.find('h3')
        summary = li.find('p')
        # url = li.find(name='a').attrs['href']
        if not title:
            continue
        sql = 'insert into autohome(newstitle,news) values(?,?)'
        val = (title.text,summary.text)
        c.execute(sql,val)
        print(title.text+'\n','\t'+summary.text+'\n')
    x += 1
    conn.commit()
    conn.close()