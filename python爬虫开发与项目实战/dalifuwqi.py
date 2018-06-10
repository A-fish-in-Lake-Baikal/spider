from urllib import request,error

urls = "http://www.cosplay0.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
proxy_ip = "124.205.155.150:9090"
httphd = request.HTTPHandler(debuglevel=1)
httpshd = request.HTTPSHandler(debuglevel=1)

def use_proxy(proxy_addr,url):
    try:
        proxy = request.ProxyHandler({'http':proxy_addr})
        # opener = request.build_opener(proxy,httpshd,httphd)
        # request.install_opener(opener)
        req = request.Request(url,headers=headers)
        data = request.urlopen(req).read().decode('utf-8')
        return data
    except error.HTTPError as e:  # 通过HTTPError的子类处理‘连接不上服务器、远程URL不存在、无网络’等异常
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    except error.URLError as e:
        print(e.reason)



if __name__=='__main__':
    data = use_proxy(proxy_ip,urls)
    # print(data)
    print(data)