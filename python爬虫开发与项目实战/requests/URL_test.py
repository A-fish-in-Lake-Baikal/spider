# coding=utf-8
'''
author:马维畅
time：2018/9/12 15:03
'''

import requests


url = 'https://sso.bucea.edu.cn/sso/'

response = requests.get(url)

print(response)