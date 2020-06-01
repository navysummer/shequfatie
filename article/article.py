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
        self.url = 'https://www.yueduwen.com'
        self.headers = {
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        }
        self.get_classify()


    def get_classify(self):
        url = self.url+'/index.html'
        r = requests.get(url,headers=self.headers)
        r.encoding='gb2312'
        soup = BeautifulSoup(r.text,'lxml')
        classify_div = soup.find('div',class_='subnav')
        classify_as = classify_div.find_all('a')
        self.classifies = [{'name':x.text,'url':x.attrs['href']}for x in classify_as]
        self.classify.insert_many(self.classifies)


    def get_classifies_articles(self):
        for classify in self.classifies:
            time.sleep(5)
            self.get_classify_articles(classify['url'],classify['name'])


    def get_classify_articles(self,url,name):
        r = requests.get(url,headers=self.headers)
        r.encoding='gb2312'
        soup = BeautifulSoup(r.text,'lxml')
        listbox = soup.find('div',class_='listbox')
        mlists = listbox.find_all('div',class_='mlist')
        for x in mlists:
            time.sleep(5)
            a = x.find('div',class_='mlist-content').find('h2').find('a')
            atitle = a.text
            aurl = self.url+a.attrs['href']
            self.get_classify_article(aurl,name)
        dede_pages = soup.find('div',class_='dede_pages')    
        if dede_pages:
            next_a = dede_pages.find('a',text=u'\u4e0b\u4e00\u9875')
            if next_a:
                time.sleep(5)
                i = url.rfind('/')
                path = url[:i+1]
                next_url = path+next_a.attrs['href']
                self.get_classify_articles(next_url,name)


    def get_classify_article(self,url,name):
        rt = requests.get(url,headers=self.headers)
        rt.encoding='gb2312'
        asoup = BeautifulSoup(rt.text,'lxml')
        viewbox = asoup.find('div',class_='viewbox')
        title = '<<%s>>%s'%(name,viewbox.find('div',class_='title').find('h2').text)
        content = viewbox.find('div',class_='content').find('table').text
        print('--------------------------------------------')
        print(url)
        self.save_article(title,content,name)


    def save_article(self,title,content,aticle_type):
        arctle_info = {
            'title':title,
            'content':content,
            'type':aticle_type,
            'status':0
        }
        x = self.article.insert_one(arctle_info)
        print(x.inserted_id)


def main():
    arctle = Arctle()
    arctle.get_classifies_articles()


if __name__ == '__main__':
    main()


