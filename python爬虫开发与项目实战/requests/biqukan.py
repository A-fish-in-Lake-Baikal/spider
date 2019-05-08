# -*- coding:utf-8 -*-
import requests,json
from urllib.request import urlretrieve
import os
from datetime import datetime
from contextlib import closing
import time
class UnsplashSpider:
    def __init__(self):
        self.id_url = 'http://unsplash.com/napi/feeds/home'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/61.0.3163.79 Safari/537.36',
            'authorization': '***********'#此部分需要自行添加
        }
        self.id_lists = []
        self.download_url='https://unsplash.com/photos/{}/download?force=true'
        print("init")
    def get_ids(self):
        # target_url = 'http://unsplash.com/napi/feeds/home'
        # target_url = 'https://unsplash.com/'

        #SSLerror 通过添加 verify=False来解决
        try:
            response = requests.get(self.id_url,headers=self.header,verify=False, timeout=30)
            response.encoding = 'utf-8'
            # print(response.text)

            dic = json.loads(response.text)
            # print(dic)
            print(type(dic))
            print("next_page:{}".format(dic['next_page']))
            for each in dic['photos']:
                # print("图片ID:{}".format(each['id']))
                self.id_lists.append(each['id'])
            print("图片id读取完成")
            return self.id_lists
        except:
            print("图片id读取发生异常")
            return False
    def download(self,img_id):
        file_path = 'images'
        download_url = self.download_url.format(img_id)
        if file_path not in os.listdir():
            os.makedirs('images')
        # 2种下载方法
        # 方法1
        # urlretrieve(download_url,filename='images/'+img_id)
        # 方法2 requests文档推荐方法
        # response = requests.get(download_url, headers=self.header,verify=False, stream=True)
        # response.encoding=response.apparent_encoding
        chunk_size=1024
        with closing(requests.get(download_url, headers=self.header,verify=False, stream=True)) as response:
            file = '{}/{}.jpg'.format(file_path,img_id)
            if os.path.exists(file):
                print("图片{}.jpg已存在,跳过本次下载".format(img_id))
            else:
                try:
                    start_time = datetime.now()
                    with open(file,'ab+') as f:
                        for chunk in response.iter_content(chunk_size = chunk_size):
                            f.write(chunk)
                            f.flush()
                    end_time = datetime.now()
                    sec = (end_time - start_time).seconds
                    print("下载图片{}完成,耗时:{}s".format(img_id,sec))
                except:
                    print("下载图片{}失败".format(img_id))



if __name__=='__main__':
    us = UnsplashSpider()
    id_lists = us.get_ids()
    if not id_lists is False:
        for id in id_lists:
            us.download(id)
            #合理的延时,以尊敬网站
            time.sleep(1)