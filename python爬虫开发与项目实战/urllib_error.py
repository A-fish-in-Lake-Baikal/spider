from urllib import request,error

try:
    req = request.urlopen("http://blog.csdn.net/blogdevteam/article/details").read().decode('utf-8')
except error.HTTPError as e: #通过HTTPError的子类处理‘连接不上服务器、远程URL不存在、无网络’等异常
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('successfully')