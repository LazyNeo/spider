# -*- coding:utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup
import tool
class Spider:
    # 页面初始化
    def __init__(self):
        self.tool = tool.Tool()
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
                    img = item.find("div",{"class":"author"}).img
                    if img.parent.name == 'a':
                        print img['src']
                        self.tool.saveImg(img['src'],img['alt'] + '.jpg')
                    else :
                        print img['alt']
                    print content.get_text()
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
            
spider = Spider()
for i in range(2,50):
    spider.getPage(i)