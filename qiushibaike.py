# -*- coding:utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup
import tool
class Spider:
    # 页面初始化
    def __init__(self):
        self.tool = tool.Tool()
        self.num = 0
    def getPage (self, page):
        url = 'http://www.qiushibaike.com/8hr/page/%s/?s=4940449' %page
        print url
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
        referer = url
        headers = {'User-Agent':user_agent,'Referer':referer}
        try:
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request)
            object_bs = BeautifulSoup(response.read())
            items = object_bs.body.find_all("div",{"class":"article block untagged mb15"})
            for item in items:
                if item.find("div",{"class":"thumb"}) == None:
                    content = item.find("div",{"class":"content"})
                    print content.get_text().encode('GBK', 'ignore')
            imgs = object_bs.body.find_all("img")
            for img in imgs:
                if 'static' not in img['src']:
                    print img['src'].encode('GBK', 'ignore')
                    print img['alt'].encode('GBK', 'ignore')
                    print self.tool.strFilter(img['alt']).encode('GBK', 'ignore')
                    self.num += 1
                    print self.num
                    self.tool.saveImg(img['src'],"img/" + self.tool.strFilter(img['alt']) + '.jpg')
                else :
                    print img['src'].encode('GBK', 'ignore')
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
    def test(self):
        return self.tool.strFilter('神马\\"卡哇伊')
spider = Spider()
# print spider.test()
for i in range(1,50):
    spider.getPage(i)
