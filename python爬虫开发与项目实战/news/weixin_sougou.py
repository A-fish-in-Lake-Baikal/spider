import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://weixin.sogou.com/'
headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.62 Safari/537.36'}

response = requests.get(url,headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')
a = soup.find_all('a')
# print(response.text)
for link in a:
    lin = link.attrs['href'].replace('javascript:void(0);','')
    print(lin)