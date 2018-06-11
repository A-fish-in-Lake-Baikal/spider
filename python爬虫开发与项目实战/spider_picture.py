from urllib import request
import re
import ssl
import os

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

if __name__=='__main__':
    urls = ['https://www.xitmi.com/tag/fuli/page{}'.format(str(i)) for i in range(1,6)]
    path = os.path.abspath('.')
    for url in urls:
        linklist = getlink(url)
        for link in linklist:
            with open(path+"//status.txt","a") as file:
                file.write(link[0]+'\n')
            print(link[0])