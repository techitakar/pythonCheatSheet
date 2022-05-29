# The requests module allows you to send HTTP requests using Python.
import requests

url='https://w3schools.com/python/demopage.htm'
reqs = requests.get(url) #reqs is a class

print(reqs.content)#returns in raw bytecode
print(reqs.text)
print(reqs.cookies)
print(reqs.encoding)
print(reqs.headers)
print(reqs.headers['Date'])
print(reqs.request)
print(reqs.url)

#alternatively you can set those meta data yourself
headers={"user-Agents":"Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"}
cookies="id=a3fWa"
reqs2=requests.get(url,headers=headers)#,cookies=cookies)

#u can send different type of requests 
'''
requests.delete(url,args)
requests.patch(url,args)
requests.post(url,data,json,args)
requests.put(url,data,args)

postReq=requests.post(url,data,json,args)
print(type(postReq))
print(dir(postReq))
'''