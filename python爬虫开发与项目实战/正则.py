import re
from urllib import request

url = "http://home.baidu.com/"
data = request.urlopen(url).read().decode('utf-8')
result1 = re.findall(r'[http]+://[^\s]+.com',data)
result2 = re.findall(r'[\w\d]+@[\w\d\.-]+',data)
for p in result1:
    print(p)
for x in result2:
    print(x)
# pattern = '\wpython\w'
# string = "sadpython1351"
# result = re.search(pattern,string)
# print(result)