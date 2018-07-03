from urllib import request



def geturls(url,proxy_hander):
    opener = request.build_opener(proxy_hander)
    response = opener.open(url)
    print(response.read())

if __name__=='__main__':
    proxy = request.ProxyHandler({"http" : "http://60.255.186.169:8888"})
    url = 'http://httpbin.org/get'
    geturls(url,proxy)