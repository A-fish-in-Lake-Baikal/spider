import requests
import re
import lxml
from bs4 import BeautifulSoup
from multiprocessing import Pool
from requests.exceptions import RequestException

def get_one_page(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'uuid=1A6E888B4A4B29B16FBA1299108DBE9C4D5DD31CEA96F18480D60BE2F1463CFC; _csrf=57563b9cf08d670d4578f91dac2bfdb64ba2cf226f8bac134d3fb299ee04fa19; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1648966199bc8-0e467625cdf926-39614101-384000-1648966199bc8; _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9C4D5DD31CEA96F18480D60BE2F1463CFC; __mta=150732297.1531313527304.1531313630392.1531313641391.5; _lxsdk_s=1648966199c-693-a01-baf%7C%7C12',
        'Host': 'maoyan.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers,timeout=1)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    dd = soup.find_all('dd')
    for d in dd:
        serials = d.find_all(class_='board-index')
        titles = d.find_all('a')
        stars = d.find_all(class_='star')
        releasetimes  = d.find_all(class_='releasetime')
        integers = d.find_all(class_='integer')
        fractions = d.find_all(class_='fraction')
        for (serial,title,star,releasetime,integer,fraction) in zip(serials,titles,stars,releasetimes,integers,fractions):
            print('*' *150)
            print(serial.text,title['title'],star.text,releasetime.text,integer.text+fraction.text)

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    parse_one_page(html)
    # print(html)

if __name__=='__main__':
    # for i in range(0,10):
    #     main(i*10)
        pool = Pool()
        pool.map(main,[i*10 for i in range(10)])
