from urllib import request
from bs4 import BeautifulSoup



def geturls(url,proxy_hander):
    opener = request.build_opener(proxy_hander)
    response = opener.open(url)
    print(response.read())
    '''soup = BeautifulSoup(response,'html.parser')
    a_list = soup.findAll('a')
    return a_list'''

if __name__=='__main__':
    proxy = request.ProxyHandler({"http" : "122.243.13.89:9000"})
    # url = 'http://news.sina.com.cn/'
    url = 'http://httpbin.org/get'
    # urls = geturls(url,proxy_hander)
    geturls(url,proxy)
    '''for newurl in urls:
        if not newurl:
            continue
        print(newurl.get('href'))'''