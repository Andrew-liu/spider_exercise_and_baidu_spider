#!/usr/bin/python2
# -*- coding:utf-8 -*-
"""
最简单的百度贴吧爬虫

Anthor: Andrew Liu
Version: 0.0.1
Date: 2014-11-29
Language: Python2.7.8
Editor: Sublime Text2
Operate: input url without page number, setup the begin page number and the end page number
function: download all text and store with the format of html
"""
import string
import urllib
import urllib2
import cookielib

def baidu_tieba(url, begin_page, end_page):
    """crawl webpage from baidu baidu_tieba

    indicate page number to crawl webpage's html text from block which come from baidu tieba
    
    Args:
        url: someone baidu tieba link without the page number
        begin_page: the begin page number what you want to crawl
        end_page: the end page number what you want to crawl

    Raise:
        URLError: a error the website can't open normally
    """
    for i in range(begin_page - 1, end_page):
        file_name = string.zfill((i + 1), 5) + '.html'  #自动生成六位文件名的html文件
        print '正在下载第' + str(i + 1) + '个网页, 并讲其存储为' + file_name + '....'
        with open(file_name, 'w+') as my_file:
            try:
                text = urllib2.urlopen((url + str(i * 50))).read()
            except urllib2.URLError, e:
                if hasattr(e, "code"):
                    print "The server couldn't fulfill the request."
                    print "Error code: %s" % e.code
                elif hasattr(e, "reason"):
                    print "We failed to reach a server. Please your url and read the Reason"
                    print "Reason: %s" % e.reason
            my_file.write(text)


def main():
    baidu_url = str(raw_input('请输入百度贴吧的地址,去掉pn=最后的数字 > '))
    begin_page = int(raw_input('请输入要下载的开始页码 > '))
    end_page = int(raw_input('请输入要下载的结束页码 > '))
    baidu_tieba(baidu_url, begin_page, end_page)



if __name__ == '__main__':
    main()