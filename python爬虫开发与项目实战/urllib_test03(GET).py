import os
from urllib import request

url = 'https://www.baidu.com/s?wd=selenium'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
path = os.path.abspath('.')

page = request.Request(url,headers=headers)
page_info = request.urlopen(page,timeout=1).read()
page_infos = page_info.decode('utf-8')
with open(path+'\\baidu_search.html',"wb") as file:
    file.write(page_info)
print(page_infos)
