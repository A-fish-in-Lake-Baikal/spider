from bs4 import BeautifulSoup
import requests

url = 'http://news.sina.com.cn'
response = requests.get(url)
response.encoding='utf-8'
print(response.text)

soup = BeautifulSoup(response.text,'html.parser')
aa = soup.find_all('a')
for a in aa:
    if a:
        print(a.text)
        link = a['href']
        print(link)
# print(soup.prettify())
# print(soup.title.text)
# print(soup.body.attrs['link'])