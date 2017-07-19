#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: Lightwitness
@contact: 498969498@qq.com
@software: PyCharm
@file: gupiao.py
@time: 2017/7/19 22:30
"""
import requests

import json

def req(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)' \
		'Chrome/59.0.3071.115 Safari/537.36',
		'Host': 'query.sse.com.cn',
		'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/',

	}
	r = requests.get(url, headers=headers)
	r.encoding = 'utf-8'
	d = json.loads(r.text)
	write_fp(d)

def write_fp(item):
		jStr = json.dumps(item, ensure_ascii=False)
		str = jStr.encode('Utf-8')

		with open('./duanzi.json', 'a') as f:
			f.write(str + '\n')
			print '保存成功'


if __name__ == '__main__':
	url= 'http://query.sse.com.cn/security/stock/getStockListData2.do?'\
		 '&isPagination=true'\
		 '&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage={0}'\
		 '&pageHelp.pageSize={1}&pageHelp.pageNo={2}&pageHelp.endPage=21&_=1500475381199'


	beginPage = 1
	pageSize = 25
	pageNo = 2
	format_url = url.format(beginPage, pageSize, pageNo)

	text = req(format_url)
