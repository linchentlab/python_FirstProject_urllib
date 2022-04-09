import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))