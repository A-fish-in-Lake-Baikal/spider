from urllib import request
from bs4 import BeautifulSoup



def geturls(url):
    response = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(response,'html.parser')
    a_list = soup.findAll('a')
    return a_list

if __name__=='__main__':
    url = 'http://news.sina.com.cn/'
    urls = geturls(url)
    for newurl in urls:
        if not newurl:
            continue
        print(newurl.get('href'))