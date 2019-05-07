from urllib import request
import re
import os
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
def getlink(url):
    global headers
    file = request.Request(url,headers=headers)
    page = request.urlopen(file)
    data = str(page.read())
    pat = '(https?://[^\s)";]+\.(\w|/)+.html)'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link
def getpic(link):
    global headers
    file1 = request.Request(link,headers=headers)
    page1 = request.urlopen(file1)
    data1 = str(page1.read())
    pattern = '(https?://[^\s)";]+\.(\w|/)+(.jpg|.png|.gif))'
    piclinks = re.compile(pattern).findall(data1)
    piclinks = list(set(piclinks))
    return piclinks

if __name__=='__main__':
    urls = ['https://www.xitmi.com/tag/fuli/page{}'.format(str(i)) for i in range(1,9)]
    path = os.path.abspath('.')
    for url in urls:
        linklist = getlink(url)
        for link in linklist:
            with open(path+"//status.txt","a") as file:
                file.write(link[0]+'\n')
            print(link[0])
            piclink = getpic(link[0])
            for p in piclink:
                request.urlretrieve(p[0],".\pic"+ r'\%s.jpg' % time.time())
                with open(path + "//status.txt", "a") as file:
                    file.write('\t'+p[0] + '\n')
                print(p[0])