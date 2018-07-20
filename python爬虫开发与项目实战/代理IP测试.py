from urllib import request
import requests
import time

PROXY_POOL_URL = 'http://192.168.1.63:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            print("proxy-ip:"+response.text)
            return response.text
    except ConnectionError:
        return None


def geturls(url,proxy_hander):

    opener = request.build_opener(proxy_hander)
    response = opener.open(url)
    print(response.read())

if __name__=='__main__':
    time1 = time.time()
    ip = get_proxy()
    proxy = request.ProxyHandler({"http" : "http://"+ip})
    url = 'http://httpbin.org/get'
    geturls(url,proxy)
    time2 = time.time()
    times = time2-time1
    print(times)