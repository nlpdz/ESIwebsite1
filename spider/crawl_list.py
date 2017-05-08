# -*- coding:utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup
# Create your spiders here

# http://www.lib.wust.edu.cn/resource/Purchased.aspx
# 进入图书馆校内访问SCI数据库连接http://www.lib.wust.edu.cn/resource/temp.aspx?type=p&id=33&url=http://www.webofscience.com/
# 这个是整个爬虫的入口，如果此链接改变需要在此处修改
class ESIspider():
    def __init__(self):
        ESIspider.LibDbUrl = "http://baike.baidu.com/item/%E8%B6%B3%E7%90%83/122380"
    def get_SCIurl(self):
        html = urlopen(ESIspider.LibDbUrl)
        bsObj = BeautifulSoup(html,"lxml")
        for link in bsObj.find_all(attrs={'class':'para'}) :
            print link.text
esi = ESIspider()
esi.get_SCIurl()


