#!/usr/bin/python
# -*- coding: UTF-8 -*

import time
import requests
from bs4 import BeautifulSoup



class Qianxiaoyanran(object):
    def __init__(self,user,password,url='http://lyf1314.com'):
        self.user = user
        self.password = password
        self.url = url
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "40",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "lyf1314.com",
            "Origin": "http://lyf1314.com",
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
        fatie_url = self.url+'/bbs/topic_add.aspx?id=846'
        fatie_data = {
            'name': title,
            'namea': 0,
            'pxa': 'var snow = new snowFall({maxFlake:30});',
            'span1': 'x-sign',
            'dtext': content,
            'h1': 2,
            'bj':'',
            'draft': 0,
            'act': '确定发表'
        }
        r = requests.post(fatie_url,cookies=self.cookies,data=fatie_data)
        return r

    def huitie(self,tid,content):
        huitie_url='%s/xml/bbs/reply_add.aspx?id=%s'%(self.url,tid)
        huitie_data = {
            'act': 'ok',
            'cont': content,
            'g': '发表'
        }
        r = requests.post(huitie_url,cookies=self.cookies,data=huitie_data)
        return r

