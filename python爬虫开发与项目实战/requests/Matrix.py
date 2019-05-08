# _*_ CODING:UTF-8 _*_
'''
@authot:马维畅
@time:2019/5/6 21:45
'''
import requests
from bs4 import BeautifulSoup



def getresponse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }
    response = requests.get(url,headers=headers,timeout=1)

    try:
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            html = response.text
            html = html.encode("utf-8")
            # with open(r"./matrix.html","w+b") as f:
            #     f.write(html)
            # print(response.text)
            soup = BeautifulSoup(html,'lxml')
            dls = soup.find_all("article")
            print(dls)
            # for dl in dls:
            #     print(dl)
    except:
        return None



if __name__ == '__main__':
    urls = ['https://www.xitmi.com/ask/page/{}'.format(str(i)) for i in range(1,15)]
    for url in urls:
        print(url)
        text = getresponse(url)
        with open("./xitmi.txt","ab+") as f:
            url = url.encode("utf-8")
            f.write(url+b'\n')