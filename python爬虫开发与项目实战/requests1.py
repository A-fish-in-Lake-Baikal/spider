import requests
from requests.exceptions import ConnectionError

url = 'http://www.httpbin.org/get'
headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
'''
# data = {
#     'name':'maweic',
#     'age':'33'
# }
response = requests.get('https://assets-cdn.github.com/images/modules/site/integrators/travis-ci.png')
with open('travis-ci.png','wb') as f:
    f.write(response.content)

file = {'file':open('travis-ci.png','rb')}
response = requests.post('http://www.httpbin.org/post',files=file,headers=headers)



print(response.text)
'''
# 获取cookies
'''
response = requests.get('http://www.baidu.com')

print(response.cookies)
for key,value in response.cookies.items():
    print(key+'='+value)'''
# 使用request.session()对象维持会话状态
'''s = requests.session()
s.get('http://www.httpbin.org/cookies/set/number/123456789')
response = s.get('http://www.httpbin.org/cookies')
print(response.text)'''

# 证书验证
'''#urllib3.disable_warnings()  #忽略警告信息
response = requests.get('https://www.httpbin.org/get',proxies=proxies)
print(response.text)'''

# 設置代理
'''proxies = {"http":"http://user:password@222.219.168.188:4536","http":"http://user:password@42.242.137.126:4531"}
response = requests.get('http://www.httpbin.org/get',proxies=proxies)
print(response.text)'''

# 超時設置
try:
    response = requests.get(url,timeout=1)
    print(response.status_code)
except ConnectionError:
    print('TimeOut')
