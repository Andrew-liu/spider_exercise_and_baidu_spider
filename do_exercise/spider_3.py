# -*- coding:utf-8 -*-
import urllib2

#创建一个密码管理者
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

#添加用户名和密码
top_level_url = "http://example.com/foo/"

#如果知道realm, 可以用来代替None
password_mgr.add_password(None, top_level_url, 'username', 'password')

#创建一个新的Hanlder
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

#创建opener
opener = urllib2.build_opener(handler)

a_url = 'http://www.baidu.com/'

#使用opener获取一个url
opener.open(a_url)

#安装opener, 此后调用urrlib2.urlopen将用自定义opener
urllib2.install_opener(opener)
