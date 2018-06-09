from urllib import request

urls = 'https://www.baidu.com/s?wd=selenium'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
proxy_ip = '115.218.126.42:9000'

def use_proxy(proxy_addr,url):
    proxy = request.ProxyHandler({'http':proxy_addr})
    opener = request.build_opener(proxy,request.HTTPHandler)
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf-8')
    return data

if __name__=='__main__':
    data = use_proxy(proxy_ip,urls)
    print(data)
    print(len(data))