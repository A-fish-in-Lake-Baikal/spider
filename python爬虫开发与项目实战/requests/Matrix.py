# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2019/5/6 21:45
'''
import requests
import sqlite3
import time
from bs4 import BeautifulSoup



def getresponse(url):

    datatime = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }
    response = requests.get(url,headers=headers,timeout=5)

    try:
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            html = response.text
            html = html.encode("utf-8")
            soup = BeautifulSoup(html,'lxml')
            articles = soup.find_all("article")
            for article in articles:
                hs = article.find_all('header')
                for h in hs:
                    al = h.find_all(target='_blank')
                    for a in al:
                        sql = 'insert into xitmi(title,furl,times) values(?,?,?)'
                        title = a.string
                        vla = (title,url,datatime)
                        c.execute(sql,vla)
                        print('写入完成...')
                        conn.commit()
        conn.close()
                        # print(a.string)
                        # print(a.title)
                    # h2s = h.find_all('h2')
                    # for h2 in h2s:
                    #     print(h2)
    except:
        return None

# def write_sql(title,url):



if __name__ == '__main__':

    urls = ['https://www.xitmi.com/page/{}'.format(str(i)) for i in range(1,10)]
    for url in urls:
        print(url)
        text = getresponse(url)
        with open("./xitmi.txt","ab+") as f:
            url = url.encode("utf-8")
            f.write(url+b'\n')
