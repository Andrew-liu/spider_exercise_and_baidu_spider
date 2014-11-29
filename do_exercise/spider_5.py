#!/usr/bin/python2
# -*- coding:utf-8 -*- 

from urllib2 import Request, urlopen, URLError, HTTPError

def main() :
    req = Request("http://www.zhihu.com")
    try:
        response = urlopen(req)
    except URLError, e :
        if hasattr(e, "code"):
            print "The server couldn't fulfill the request."
            print "Error code: %s" % e.code
        elif hasattr(e, "reason"):
            print "We failed to reach a server."
            print "Reason: %s" % e.reason
    else :
        print "No exception was raised."
    print response.read()   #读取了页面的html代码

if __name__ == '__main__':
    main()

