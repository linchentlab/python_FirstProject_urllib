import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen("http://www.baidu.com",timeout = 0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("Time Out")