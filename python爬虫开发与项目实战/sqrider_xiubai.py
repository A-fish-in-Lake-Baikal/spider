from urllib import request
import re

def geturl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    page = request.Request(url,headers=headers)
    pages = request.urlopen(page)
    data = pages.read().decode('utf-8')
    pat = '<div class="content">(.*?)</div>'
    contentlist = re.compile(pat,re.S).findall(data)
    x=1
    for content in contentlist:
        keys = ["<span>","\n","</span>",":&quot;","<br/>"]
        for key in keys:
            content = content.replace(key,"")
        x += 1
        print('-' *200)
        print(content)

if __name__=='__main__':
    urls = ['https://www.qiushibaike.com/8hr/page/{}'.format(str(i)) for i in range(1,14)]
    for url in urls:
        print(url)
        geturl(url)

