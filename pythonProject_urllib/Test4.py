import urllib.request

response = urllib.request.urlopen("http://www.baidu.com",timeout = 0.1)
print(response.read())
'''
task= open("C:\Deutsche Bundesbank\Bundesbank.txt","a")

print (task.write("Deutsche Bundesbank Researchers and Citations\n"))

print(task.write(year, citation))

task.close()
'''