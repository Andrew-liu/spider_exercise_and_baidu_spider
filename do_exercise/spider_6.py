#!/usr/bin/python2
# -*- coding:utf-8 -*-
"""
    程序中使用Proxy代理, 使程序不受环境影响
"""
import urllib
import urllib2
import cookielib

def main():
    """

    设置代理Proxy
    """
    enable_proxy = True
    proxy_handler = urllib2.ProxyHandler({"http" : "http://some-proxy.com:8080"})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)

def time_out():
    """
    
    通过urlopen中的参数设置Timeout属性
    """
    try:
        response = urllib2.urlopen("http://www.google.com", timeout = 10)
    except urllib2.URLError, e :
        if hasattr(e, "code"):
            print "The server couldn't fulfill the request."
            print "Error code: %s" % e.code
        elif hasattr(e, "reason"):
            print "We failed to reach a server."
            print "Reason: %s" % e.reason

def add_my_header():
    request = urllib2.Request("http//www.baidu.com")
    request.add_header("User-Agent", "fake-client")
    response = urllib2.urlopen(request)
    response.read()

def my_redirect():
    """

    只需要检查一下Request的url和response的url
    """
    my_url = "http://www.baidu.com"
    response = urllib2.urlopen(my_url)
    redirected = response.geturl() == my_url
    print redirected

def get_cookie():
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open("http://www.baidu.com")
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value 

def get_code():
    try:
        response = urllib2.urlopen("http://www.baidu.com")
    except urllib2.HTTPError, e:
        print e.code
    print response.getcode()

def debug_log():
    http_handler = urllib2.HTTPHandler(debuglevel = 1)
    https_handler = urllib2.HTTPSHandler(debuglevel = 1)
    opener = urllib2.build_opener(http_handler, https_handler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen("http://www.baidu.com")

def form_login():
    post_data = urllib.urlencode({
        'username': '汪小光',
        'password': 'why888',
        'continueURI': 'http://www.verycd.com/',
        'fk': '',
        'login_submit': '登陆'
    })
    req = urllib2.Request(url = "http://secure.verycd.com/signin", data = post_data)
    result = urllib2.urlopen(req)
    print result.read()

def imitate_browser():
    """

    伪装成浏览器
    """
    post_data = urllib.urlencode({
        'username': '汪小光',
        'password': 'why888',
        'continueURI': 'http://www.verycd.com/',
        'fk': '',
        'login_submit': '登陆'
    })
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6' 
    }
    req = urllib2.Request(
    url = 'http://secure.verycd.com/signin/*/http://www.verycd.com/',
    data = post_data, 
    headers = headers
    )
    result = urllib2.urlopen(req)
    print result.read()

def reverse_link():
    """

    反盗链, 查看头部referer是否为访问的网站
    """
    post_data = urllib.urlencode({
        'username': '汪小光',
        'password': 'why888',
        'continueURI': 'http://www.verycd.com/',
        'fk': '',
        'login_submit': '登陆'
    })
    headers = {
    'Referer': 'http://www.cnbeta.com/articles'
    }
    req = urllib2.Request(
    url = 'http://www.cnbeta.com'
    )
    try:
        result = urllib2.urlopen(req)
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print "The server couldn't fulfill the request."
            print "Error code: %s" % e.code
        elif hasattr(e, "reason"):
            print "We failed to reach a server."
            print "Reason: %s" % e.reason
    print result.read()

if __name__ == '__main__':
    reverse_link()

