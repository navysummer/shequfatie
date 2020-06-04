#!/usr/bin/python
# -*- coding: UTF-8 -*
import time
from shequ import Qianxiaoyanran


class QianxiaoyanranHuitie(object):
    def __init__(self):
        self.qxyr = Qianxiaoyanran('10198','xia990722')
    def huitie(self):
        for i in range(100):
            time.sleep(5)
            r=self.qxyr.huitie('5617',i)
            print(r.url)

def main():
    qx=QianxiaoyanranHuitie()
    qx.huitie()

if __name__ == '__main__':
    main()