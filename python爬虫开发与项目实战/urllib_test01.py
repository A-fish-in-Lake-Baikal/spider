import urllib.request
import os

file = urllib.request.urlopen("http://www.sina.com.cn")
files = file.read()
# file = file.decode('utf-8')
path = os.path.abspath('.')+''
print(path)
with open(path+"\\sina.html","wb") as f:
    f.write(files)

print(file.info)
print(file.getcode())