import urllib.request
from urllib import request

url = 'http://picture.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
req = request.Request(url,headers=headers)
for i in range(1,100):
    try:
        file = urllib.request.urlopen(req,timeout=0.1).read()
        file = file.decode('utf-8')
        print(len(file))
    except Exception as e:
        print('出现异常-->'+str(e))
print(i)