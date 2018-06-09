import urllib.request
import os

file = urllib.request.urlopen("http://www.sina.com.cn")
files = file.read()
# file = file.decode('utf-8')
path = os.path.abspath('.')

print(path)
with open(path+"\\sina.html","wb") as f:
    f.write(files)


# 返回与当前环境相关的信息
print(file.info())
# 获取当前爬取网页的状态码
print(file.getcode())
# 获取当前爬取网页的URL
print(file.geturl())