#coding:utf-8
import requests
from datetime import *
import time
from BeautifulSoup import BeautifulSoup
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
_param={
	'start':1430383878
}
_zhihu_url = 'http://www.zhihu.com/people/zhoumengmeng'
_rep = requests.get(_zhihu_url,params=_param)
_content = _rep.content
_content_soup = BeautifulSoup(_content)
_items = _content_soup.findAll('div',{'class':'zm-profile-section-item zm-item clearfix'})
for _item in _items:
	#_time = _item.find('span',{'class':'zm-profile-setion-time zg-gray zg-right'})
	_time = _item['data-time']
	_title = _item.find('a',{'class':'question_link'})
	try:
		print '%s  :  %s' %( time.strftime( "%Y-%m-%d %H:%M:%S",time.localtime( int(_time) ) ),_title.text )
	except Exception,e:
		print Exception,':',e