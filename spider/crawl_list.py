# -*- coding:utf-8 -*-
import re
from urllib import urlopen
from bs4 import BeautifulSoup

# Create your spiders here

# http://www.lib.wust.edu.cn/resource/Purchased.aspx
# 进入图书馆校内访问SCI数据库连接http://www.lib.wust.edu.cn/resource/temp.aspx?type=p&id=33&url=http://www.webofscience.com/
# 这个是整个爬虫的入口，如果此链接改变需要在此处修改
class ESIspider():
    def __init__(self):
        ESIspider.LibDbUrl = "http://www.cnblogs.com/kuqs/"
    def get_SCIurl(self):
        html = urlopen(ESIspider.LibDbUrl)
        bsObj = BeautifulSoup(html,"lxml")
        list = bsObj.find_all("div", class_ =  'day')
        if list:
            for item in list:
                title = item.find("a", class_ =  'postTitle2').text
                context = item.find("div", class_ =  'c_b_p_desc').text
                author = re.sub(ur"[阅读评论编辑]+|[^\u4e00-\u9fa5]+", "", item.find("div", class_='postDesc').text)
                publication = "博客园"
                print title, context, author, publication
                return title, context, author, publication
                EsiDissertation.objects.create(title=title, author=author, context=context, publication=publication)
        else:
            return "title", "context", "author", "publication"
