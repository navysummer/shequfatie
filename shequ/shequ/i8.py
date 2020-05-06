#!/usr/bin/python
# -*- coding: UTF-8 -*

import time
import requests
from bs4 import BeautifulSoup

class I8(object):
    """docstring for I8"""
    def __init__(self, user,password,url='http://h5.pinpinhu.com'):
        self.user = user
        self.password = password
        self.url = url
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            'Cache-Control': 'max-age=0',
            'Content-Type': 'application/x-www-form-urlencoded',
            "Host": "h5.pinpinhu.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        }
        self.login()

    def login(self):
        login_url = self.url+'/loginValidate.action'
        login_data = {
            'account':self.user,
            'password':self.password
        }
        r = requests.post(login_url,headers=self.headers,data=login_data)
        self.cookies = r.cookies
        print(r.text)

