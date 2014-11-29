# -*- coding:utf-8 -*-
import urllib2
import urllib

url = "http://www.someserver.com/register.cgi"

values = {
	'name' : 'Andrew',
	'location' : 'NJU',
	'language' : 'Python'
}

data = urllib.urlencode(values) #data数据需要编码成标准形式
print data
req = urllib2.Request(url, data) #发送请求同时传送data表单
reponse = urllib2.urlopen(req) #接受反馈数据
html = reponse.read() #读取反馈数据

"""
full_url = url + '?' + data
data = urllib2.open(full_url)
"""