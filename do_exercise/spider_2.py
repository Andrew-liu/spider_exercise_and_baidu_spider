import urllib2
"""
req = urllib2.Request("http://www.baidusss.com/")
try :
	urllib2.urlopen(req)
except urllib2.URLError, e :
	print e.reason
"""
req = urllib2.Request("http://bbs.csdn.net/callmewhy")
try:
	urllib2.urlopen(req)
except urllib2.HTTPError, e:
	print e.code
	#print e.read()
