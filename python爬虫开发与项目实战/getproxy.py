from urllib import request
from bs4 import BeautifulSoup
import zlib
import time
import sqlite3

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
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        for td in td_list:
            # 找出IP
            if td.text=='':
                continue
            else:
                if td.attrs['data-title']=='IP':
                    ip = td.text
                    print(ip)
                # 找出端口
                elif td.attrs['data-title']=='PORT':
                    dk = td.text
                    print(dk)
                elif td.attrs['data-title']=='匿名度':
                    nimd = td.text
                    print(nimd)
                elif td.attrs['data-title']=='类型':
                    leix = td.text
                    print(leix)
                elif td.attrs['data-title']=='位置':
                    weiz = td.text
                    print(weiz)
                elif td.attrs['data-title']=='响应速度':
                    xysd = td.text
                    print(xysd)
                elif td.attrs['data-title']=='最后验证时间':
                    zhyzsj = td.text
                    print(zhyzsj)
                    sql = 'insert into proxy(Ip,Port,Anonymity,Type,Position,Responsespeed,Finalverificationtime) values(?,?,?,?,?,?,?)'
                    val = (ip,dk,nimd,leix,weiz,xysd,zhyzsj)
                    c.execute(sql,val)
                    conn.commit()
                    conn.close()

        #     with open(r'./proxyip.txt','a') as file:
        #         file.write('\t'+td.text+'\n' )
        time.sleep(0.5)
'''try:
    html = gzip.decompress(page).decode('gb18030')
    print(html)
except:
    # html = page.decode('utf-8')
    pass


'''