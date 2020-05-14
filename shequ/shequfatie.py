#!/usr/bin/python
# -*- coding: UTF-8 -*

import time
import pymongo
import requests
from bs4 import BeautifulSoup
from shequ import Qqw,Hongchen,Mengxue,Shiguang,Txqq,Xingangwan,Yuluohongchen,Zimeng,I8,Qianxiaoyanran

class SQ(object):
    """docstring for Fatie"""
    def __init__(self):
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.articledb = self.myclient["article"]
        self.article = self.articledb["article"]
        self.login()

    def login(self):
        self.qqw = Qqw('10342','xia990722')
        self.hongchen = Hongchen('10137','xia990722')
        self.mengxue = Mengxue('11377','xia990722')
        self.shiguang = Shiguang('888888','xia990722')
        #self.txqq = Txqq('72365','xia990722')
        self.xingangwan = Xingangwan('12200','xia990722')
        self.yuluohongchen = Yuluohongchen('1001','xia990722')
        self.zimeng = Zimeng('10129','xia990722')
        # self.i8 = I8('navysummer','xia990722')
        self.qxyr = Qianxiaoyanran('10198','xia990722')


    def operate(self):
        article = self.article.find_one({'status':0},{ "_id": 0, "title": 1, "content": 1,"status":1 })
        if article:
            self.fatie(article['title'],article['content'].replace('\n','{br}        '))


    def fatie(self,title,content):
        print('----------------------------------------------------------')
        print({'title':title})
        qqw_info = self.qqw.fatie(title,content)
        print({'url':qqw_info.url,'status':qqw_info.text.find(u'\u6210\u529f')})
        hongchen_info = self.hongchen.fatie(title,content)
        print({'url':hongchen_info.url,'status':hongchen_info.text.find(u'\u6210\u529f')})
        mengxue_info = self.mengxue.fatie(title,content)
        print({'url':mengxue_info.url,'status':mengxue_info.text.find(u'\u6210\u529f')})
        shiguang_info = self.shiguang.fatie(title,content)
        print({'url':shiguang_info.url,'status':shiguang_info.text.find(u'\u6210\u529f')})
        #txqq_info = self.txqq.fatie(title,content)
        #print({'url':txqq_info.url,'status':txqq_info.text.find(u'\u6210\u529f')})
        xingangwan_info = self.xingangwan.fatie(title,content)
        print({'url':xingangwan_info.url,'status':xingangwan_info.text.find(u'\u6210\u529f')})
        yuluohongchen_info = self.yuluohongchen.fatie(title,content)
        print({'url':yuluohongchen_info.url,'status':yuluohongchen_info.text.find(u'\u6210\u529f')})
        zimeng_info = self.zimeng.fatie(title,content)
        print({'url':zimeng_info.url,'status':zimeng_info.text.find(u'\u6210\u529f')})
        qianxiaoyanran_info = self.qxyr.fatie(title,content)
        print({'url':qianxiaoyanran_info.url,'status':qianxiaoyanran_info.text.find(u'\u6210\u529f')})
        self.article.update_one({'title':title},{ "$set": {'status':1} })



def main():
    sq = SQ()
    sq.operate()


if __name__ == '__main__':
    main()

