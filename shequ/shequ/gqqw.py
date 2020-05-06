#!/usr/bin/python
# -*- coding: UTF-8 -*

import time
import requests
from bs4 import BeautifulSoup


class Qqw(object):
    """docstring for Qqw"""
    def __init__(self,user,password,url='http://3gqqw.com'):
        self.user = user
        self.password = password
        self.url = url
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://3gqqw.com",
            "Referer": "http://3gqqw.com/login/login.aspx",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        }
        self.login()

    def login(self):
        login_url = self.url+'/login/login.aspx'
        login_data = {
            'act':'ok',
            'srcurl':'',
            'name':self.user,
            'pass':self.password
        }
        r = requests.post(login_url,headers=self.headers,data=login_data)
        self.cookies = r.cookies


    def fatie(self,title,content):
        fatie_url=self.url+'/bbs/topic_add.aspx?id=97018'
        fatie_data = {
            'name':title,
            'dtext':content,
            'draft':'0',
            'act':'确定发表'
        }
        r = requests.post(fatie_url,cookies=self.cookies,data=fatie_data)
        return r
