import urllib.request
response = urllib.request.urlopen('http://www.python.org')
print(type(response))
