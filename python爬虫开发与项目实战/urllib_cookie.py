from urllib import request,parse
from http import cookiejar
import os

url = "http://192.168.2.39/multiMaster.aspx"
path = os.path.abspath('.')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
cook = parse.urlencode({"txtUser":"admin","txtPwd":"00000"}).encode('utf-8')

req = request.Request(url,cook,headers=headers)
data1 = request.urlopen(req).read()
with open(path+"\\1.html","wb") as file:
    file.write(data1)

url2 = "http://192.168.2.39/user_center.aspx#uc_resources"
req2 = request.Request(url2,cook,headers=headers)
cjar = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cjar))
request.install_opener(opener)
f = opener.open(req2)

data2 = f.read()
with open(path+"\\2.html","wb") as file1:
    file1.write(data2)