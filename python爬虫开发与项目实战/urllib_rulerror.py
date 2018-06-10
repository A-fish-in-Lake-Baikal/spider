from urllib import request,error

try:
    req = request.urlopen("ftp://blog.csdn.net/blogdevteam/article/details").read().decode('utf-8')
    print(req)
except error.HTTPError as e: #通过HTTPError的子类处理‘连接不上服务器、远程URL不存在、无网络’等异常
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
except error.URLError as e:
    print(e.reason)