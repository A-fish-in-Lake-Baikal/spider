from urllib import request
from bs4 import BeautifulSoup
import zlib
import time
import sqlite3
import telnetlib

urls = ['https://www.kuaidaili.com/free/inha/{}/'.format(str(i)) for i in range(1,2371)]


for url in urls:
    header = {'Accept-Encoding': 'gzip, deflate, br',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    # 添加头信息
    response = request.Request(url,headers=header)
    # 读取页面内容
    page = request.urlopen(response).read()
    # 由于服务器返回的内容经过压缩处理，所以要进行解压
    data = zlib.decompress(page,16+zlib.MAX_WBITS)
    text = data.decode('utf-8')

    soup = BeautifulSoup(text,'html.parser')
    # 找到存放数据的table
    parper = soup.find(class_="table table-bordered table-striped")
    # 找到tr标签（列表）
    tr_list = parper.find_all('tr')
    # print(text)
    # print(parper)
    # 打印出列表中每条tr
    for tr in tr_list:
        td_list = tr.find_all('td')
        print('*' *150)
        # print(td_list)
        #with open(r'./proxyip.txt','a') as f:
            #f.write(r'第%s条' %i+'\n')
        for td in td_list:
            if td.text=='':
                continue
            else:
                # 找出IP
                global ip,dk
                if td.attrs['data-title']=='IP':
                    ip=td.text
                    print(ip)
                # 找出端口
                if td.attrs['data-title']=='PORT':
                    dk = td.text
                    print(dk)
                # 测试代理ip是否可用
                    try:
                        telnetlib.Telnet(ip,dk)
                    except:
                        print('失败')
                    else:
                        print('成功！！！！')
                        with open(r'./ip.txt','a') as file:
                            file.write(ip+':'+dk+'\n')

'''try:
    html = gzip.decompress(page).decode('gb18030')
    print(html)
except:
    # html = page.decode('utf-8')
    pass
'''