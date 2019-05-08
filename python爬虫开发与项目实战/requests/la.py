import requests
import time
from bs4 import BeautifulSoup
from requests.exceptions import RequestException



def one_page(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            soup = BeautifulSoup(response.text,'lxml')
            links = soup.find_all(class_='font12 fleft')
            # print(links[0])
            for link in links:
                aa = link.find_all('a')
                pic_url = 'http://cosplay.la/'+aa[0]['href']
                get_img_link(pic_url)
    except RequestException:
        print("连接错误")
def get_img_link(link):
    try:
        print("网页链接%s" %link)
        response = requests.get(link)
        if response.status_code==200:
            soup = BeautifulSoup(response.text,'lxml')
            pp = soup.find_all(class_='mbottom10')
            for p in pp:
                img_links = p.find_all('img')
                for img_link in img_links:
                    linka=img_link['src']
                    print(linka)
                    # download(linka)
    except RequestException:
        print("连接错误")
def download(img_link):
    picture = requests.get(img_link)
    path = r'C:\pic'
    print("开始下载:%s" %img_link)
    with open(path+'\%s.jpg' %time.time(),'wb' ) as f:
        f.write(picture.content)

if __name__ == '__main__':
    for i in range(1,347):
        url = 'http://cosplay.la/photo/index/0-0-'+ str(i)
        one_page(url)

