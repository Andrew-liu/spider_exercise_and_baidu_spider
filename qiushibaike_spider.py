#!/usr/bin/python2
# -*- coding:utf-8 -*-
"""
This is a simple spider that is used to crawl someone urllib2

Anthor: Andrew Liu
Version: 0.0.1
Date: 2014-11-30
Language: Python2.7.8
Editor: Sublime Text2
Operate: use enter to show a line  in qiushibaike
"""
import re
import thread
import time
import urllib
import urllib2

class SpiderModel(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        page: it uses to indicate the current page you are crawling
        pages: it is used to store the page text 
        enabel: it is flag to express  whether crawl action are working or not
    """

    def __init__(self):
        """this is init function

        used to init class
        """
        self.page = 1
        self.pages = []
        self.enable = False

    def get_page(self, page):
        """cut page text function

        Args:
            page: it uses to indicate the current page you are crawling, which is a string 

        Returns:
            items: it stores what you have crawled text from current webpage
        """
        my_url = "http://m.qiushibaike.com/hot/page/" + page
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {'User-Agent' : user_agent}
        req = urllib2.Request(my_url, headers = headers)
        try :
            my_response = urllib2.urlopen(req)
        except urllib2.URLError, e :
            if hasattr(e, "code"):
                print "The server couldn't fulfill the request."
                print "Error code: %s" % e.code
            elif hasattr(e, "reason"):
                print "We failed to reach a server. Please your url and read the Reason"
                print "Reason: %s" % e.reason
        my_page = my_response.read()
        unicode_page = my_page.decode("utf-8")  #make utf-8 code to unicode
        my_items = re.findall(r'<div.*?class="content".*?title="(.*?)">(.*?)</div', unicode_page, re.S) 
        #re.S make . to match newline
        items = []
        for item in my_items :
            items.append([item[0].replace("\n", ""), item[1].replace("\n", "")])
        # for item in items :
        #     print "第%d页" % self.page, item[0], item[1]
        return items

    def load_page(self) :
        """load the new page 

        this function will load a new page if the user not input quit
        """
        while self.enable :
            #how much page you want to crawl
            if self.page < 2 :
                try :
                    my_page = self.get_page(str(self.page))
                    self.page += 1
                    self.pages.append(my_page)
                except urllib2.URLError, e :
                    if hasattr(e, "code"):
                        print "The server couldn't fulfill the request."
                        print "Error code: %s" % e.code
                    elif hasattr(e, "reason"):
                        print "We failed to reach a server. Please your url and read the Reason"
                        print "Reason: %s" % e.reason
                print "开始第%d次爬虫" % self.page
            else :
                time.sleep(1)

    def show_page(self, now_page, page) :
        """show the page text
        
        the function can show what you crawl text  and show it on termainal

        """
        for items in now_page :
            print "第%d页" % page, items[0], items[1]
            my_input = raw_input()
            if my_input == "quit" :
                self.enable = False
                break

    def start_spider(self):
        """start crawl action 

        the function control crawl action
        """
        self.enable = True
        page = self.page
        print "正在加载网页中...."
        thread.start_new_thread(self.load_page, ())  #build a new thread
        while self.enable :
            if self.pages :
                now_page = self.pages[0]
                del self.pages[0]
                self.show_page(now_page, page)
                page += 1

def main() :
    print """
    -----------------------------------------------

        Author : Andrew_liu
        Function : qiushibaike spider
        Version : 0.0.1
        Date : 2014-11-30
        Language : Python2.7.8
        Editor : Sublime Text2
        Operate : input quit to exit the spider
    
    ------------------------------------------------
    """
    print "按下回车键浏览今日的糗百内容 : "
    raw_input(' ')
    my_spider = SpiderModel()
    my_spider.start_spider()

if __name__ == '__main__':
    main()


