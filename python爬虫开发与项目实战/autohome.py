from urllib import request,error
from bs4 import BeautifulSoup
import sqlite3
import ssl
import time

urls = ['https://www.autohome.com.cn/news/{}/#liststart'.format(str(i)) for i in range(1,4194)]
localpath=r'./pic'
x = 1
for url in urls:
    try:
        print('第%s頁' %x)
        # url = 'https://www.autohome.com.cn/news/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
        ssl._create_default_https_context = ssl._create_unverified_context
        # 添加头信息
        file = request.Request(url,headers=headers)
        # 读取网页内容
        page = request.urlopen(file).read().decode('gbk')
        soup = BeautifulSoup(page,'html.parser')
        li_list = soup.find(id='auto-channel-lazyload-article').find_all('li')
        # 创建数据库
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        # print(li_list)
        for li in li_list:
            title = li.find('h3')
            # 如果li为空则跳过
            if not title:
                continue
            summary = li.find('p')
            url = li.find('a').attrs['href']
            url = url.replace('//','')
            img = li.find('img').attrs['src']
            img = img.replace('//','http://')
            request.urlretrieve(img,localpath+'\%s.jpg' %time.time())
            print(url)
            print(img)
            # for url_b in url_a:
            #     print(url_b)
            sql = 'insert into autohome(newstitle,news,newsurl,picurl) values(?,?,?,?)'
            val = (title.text,summary.text,url,img)
            c.execute(sql,val)
            print(title.text+'\n','\t'+summary.text+'\n')
        x += 1
        conn.commit()
        conn.close()
    except error.HTTPError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)