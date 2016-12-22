#-*- coding:utf-8 -*-
import re
import os
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
#处理页面标签类
class Tool:
    #创建新目录
    def mkdir(self,path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print u"偷偷新建了名字叫做",path,u'的文件夹'
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print u"名为",path,'的文件夹已经创建成功'
            return False
    #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL,fileName):
        try:
            u = urllib.urlopen(imageURL)
            data = u.read()
            f = open(fileName, 'wb')
            f.write(data)
            print u"正在悄悄保存她的一张图片为",fileName.encode('GBK', 'ignore')
            f.close()
        except IOError,e:
            if hasattr(e,"code"):
                print u"保存图片发生错误code",e.code.encode('GBK', 'ignore')
            if hasattr(e,"reason"):
                print u"保存图片发生错误reason",e.reason.encode('GBK', 'ignore')

    def strFilter(self, str):
        p = re.compile("[\s+\.\!\/\\\_,$%^*(+\"\'<>]+|[+——！！、？…。，，。\]\[？?、~@#￥%灬&*（）]+")
        return p.sub("",str).decode("utf8", 'ignore')
