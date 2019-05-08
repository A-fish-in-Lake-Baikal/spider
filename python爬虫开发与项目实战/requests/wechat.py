# coding=utf-8
'''
author:马维畅
time：2018/8/11 14:34
'''

import requests
from bs4 import BeautifulSoup

class WechatNews(object):
    def __init__(self,url):
        self.url = url


    def getcontent(self):
        links = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'lxml')
        aa = soup.find_all('a')
        for a in aa:
            link = a['href']
            if 'http://mp.weixin.qq.com' and 'new=1' in link:
                links.append(link)
        return links

    def getnewscontent(self):
        links = self.getcontent()
        print(links)
        x = 1
        for link in links:
            response = requests.get(link)
            with open(r'%s.html' %x,'wb') as file:
                file.write(response.text.encode('utf-8'))
            x += 1




if __name__ == '__main__':
    url = 'http://weixin.sogou.com/weixin?type=2&query=AI'
    wx = WechatNews(url)
    wx.getnewscontent()