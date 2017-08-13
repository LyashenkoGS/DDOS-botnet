import urllib2

# send an HTTP GET request
response = urllib2.urlopen("http://127.0.0.1:8080").read()
data = response.read()
print data
response.close()
