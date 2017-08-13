import urllib2

# send an HTTP GET request
response = urllib2.urlopen("http://172.0.0.10:8080")
data = response.read()
print data
response.close()
