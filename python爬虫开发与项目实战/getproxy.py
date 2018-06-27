from urllib import request
from bs4 import BeautifulSoup
import zlib

url = 'https://www.kuaidaili.com/free/inha/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
# 添加头信息
response = request.Request(url,headers=header)
# 读取页面内容
page = request.urlopen(response).read()
# 由于服务器返回的内容经过压缩处理，所以要进行解压
data = zlib.decompress(page,16+zlib.MAX_WBITS)
text = data.decode('utf-8')

soup = BeautifulSoup(text,'html.parser')
parper = soup.find(class_="table table-bordered table-striped")
tr_list = parper.find_all('tr')
# print(text)
# print(parper)
for tr in tr_list:
    td_list = tr.find_all('td')
    print('*' * 100)
    # print(td_list[0])
    for td in td_list:
        print(td.text)


'''try:
    html = gzip.decompress(page).decode('gb18030')
    print(html)
except:
    # html = page.decode('utf-8')
    pass


'''