from bs4 import BeautifulSoup
import requests

url = 'http://www.baidu.com'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify())
print(soup.title.text)
print(soup.body.attrs['link'])