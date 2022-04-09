import urllib.request,http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie1.txt',ignore_discard = True,ignore_expires = True)
#调用load方法读取本地的Cookie文件，获取Cookie内容
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))