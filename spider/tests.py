# # -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
from urllib2 import urlopen,Request

sidebardiv = urlopen('file:///C:/Users/qqs/PycharmProjects/ESIwebsite/spider/page.html').read()
sidebardiv = BeautifulSoup(sidebardiv, 'html.parser')
bibliographya = sidebardiv.find('div', id='RECORD_30')

print bibliographya.find('value', attrs={'lang_id': True}).get_text()







