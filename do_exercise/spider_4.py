from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://127.0.0.1:8000'
req = Request(old_url)
response = urlopen(req)  
print 'Info():'
print response.info()
