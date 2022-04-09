from urllib import request,parse

url = "http://www.baidu.com"
headers = {
    'User-Agent' : 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host' : "www.baidu.com"
}
dict = {'name' : 'germey'}
data = bytes(parse.urlencode(dict),encoding = 'utf-8')
req = request.Request(url = url,data = data,headers = headers,method = 'POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))