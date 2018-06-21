from urllib import request
from bs4 import BeautifulSoup
import re


url = 'https://www.autohome.com.cn/news/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
# 添加头信息
file = request.Request(url,headers=headers)
# 读取网页内容
page = request.urlopen(file).read().decode('gbk')
soup = BeautifulSoup(page,'html.parser')
li_list = soup.find(id='auto-channel-lazyload-article').find_all('li')
for li in li_list:
    title = li.find('h3')
    summary = li.find('p')
    url = li.find('a').attrs['href']
    if not title:
        continue
    print(title.text+'\n','\t'+summary.text+'\n',url)