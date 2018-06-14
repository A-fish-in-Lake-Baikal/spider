from urllib import request
import re

def geturl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    page = request.Request(url,headers=headers)
    pages = request.urlopen(page)
    data = str(pages.read())
    pat = '<div class="content">(.*?)</div>'
    link = re.compile(pat,re.S).findall(data)
    return link

if __name__=='__main__':
    urls = ['https://www.qiushibaike.com/8hr/page/{}'.format(str(i)) for i in range(1,13)]
    for url in urls:
        linklist = geturl(url)
        for link in linklist:
            link = link.replace
            print(link)
