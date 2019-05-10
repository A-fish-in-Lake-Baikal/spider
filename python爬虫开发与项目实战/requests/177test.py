# coding=utf-8
'''
author:马维畅
time：2019/5/9 14:45
'''

import requests

def getpage(url):
    responce = requests.get(url, timeout=2)
    try:
        if responce.status_code == 200:
            print("{}请求成功:{}".format(url,responce.status_code))
    except:
            print("请求失败:{}".format(responce.status_code))



if __name__=='__main__':
    urls = ["http://192.168.2.177/PictureHandle.ashx?id=1840{}&type=thumbnail".format(str(i)) for i in range(0,21)]
    while True:
        for url in urls:
            getpage(url)
