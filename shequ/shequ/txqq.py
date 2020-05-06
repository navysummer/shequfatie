#!/usr/bin/python
# -*- coding: UTF-8 -*

import time
import requests
from bs4 import BeautifulSoup

class Txqq(object):
    """docstring for Txqq"""
    def __init__(self, user,password,url='http://txqq789.com'):
        self.user = user
        self.password = password
        self.url = url
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": "txqq789.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        }
        self.login()

    def login(self):
        login_url = self.url+'/server/login.aspx?name='+self.user+'&pass='+self.password
        r = requests.get(login_url,headers=self.headers)
        status = int(r.text.split(':')[1].split("}")[0].strip())
        if not status:
            self.cookies = r.cookies


    def fatie(self,title,content):
        fatie_url = self.url + '/bbs/topic_add.aspx?id=9793'
        fatie_data = {
            'name': title,
            'dtext': content,
            'act': '发表'
        }
        r = requests.post(fatie_url,cookies=self.cookies,data=fatie_data)
        return r