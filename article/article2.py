#!/usr/bin/python
# -*- coding: UTF-8 -*

import time
import pymongo
import requests
from bs4 import BeautifulSoup

class Arctle(object):
    """docstring for Arctle"""
    def __init__(self):
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.articledb = self.myclient["article"]
        self.classify = self.articledb["classify"]
        self.article = self.articledb["article"]
        self.url = 'http://www.xigushi.com'
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Host":"www.xigushi.com",
            "If-Modified-Since":"Wed, 27 May 2020 12:30:09 GMT",
            "If-None-Match":"809e328f2234d61:19c6",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        }
        self.get_classify()


    def get_classify(self):
        url = self.url+'/index.html'
        r = requests.get(url,headers=self.headers)
        r.encoding='gb2312'
        soup = BeautifulSoup(r.text,'lxml')
        headers = soup.find('div',class_='head3').find('div',class_='header').find('div',class_='conter').find('ul').find_all('li')
        self.classifies = [{'name':li.find('a').text,'url':self.url+li.find('a').attrs['href']}for li in headers][4:]
        # print(self.classifies)
        # self.classify.insert_many(self.classifies)


    def get_classifies_articles(self):
        for classify in self.classifies:
            time.sleep(5)
            self.get_classify_articles(classify['url'],classify['name'])


    def get_classify_articles(self,url,name):
        r = requests.get(url,headers=self.headers)
        r.encoding='gb2312'
        soup = BeautifulSoup(r.text,'lxml')
        lst = soup.find('div',class_='index').find('div',class_='list')
        first = lst.find('dl').find('dd').find('ul').find('li').find('a')
        first_url = self.url+first.attrs['href']
        self.get_classify_article(first_url,name)


    def get_classify_article(self,url,name):
        rt = requests.get(url,headers=self.headers)
        rt.encoding='gb2312'
        asoup = BeautifulSoup(rt.text,'lxml')
        articleinfo = asoup.find('div',class_='index').find('div',class_='by').find('dl').find('dd')
        title = '<<%s>>%s'%(name,articleinfo.find('h1').text)
        content=''
        ps = articleinfo.find_all('p')
        for p in ps:
            content=content+p.text
        print('--------------------------------------------')
        print(url)
        self.save_article(title,content,name)
        next_page=asoup.find('div',class_='index').find('div',class_='by').find('div',class_='pages').find('div',class_='pages-left').find('ul').find_all('li')[1]
        if next_page:
            a = next_page.find('a')
            if a:
                next_url = self.url+a.attrs['href']
                time.sleep(5)
                self.get_classify_article(next_url,name)


    def save_article(self,title,content,aticle_type):
        arctle_info = {
            'title':title,
            'content':content,
            'type':aticle_type,
            'status':0
        }
        x = self.article.insert_one(arctle_info)
        # print(x.inserted_id)


def main():
    arctle = Arctle()
    arctle.get_classifies_articles()


if __name__ == '__main__':
    main()
