from bs4 import BeautifulSoup
import requests

url="https://www.electronicscomp.com/ir-sensor-module-india"
headers={"user-Agents":"Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"}

req=requests.get(url,headers=headers)
print("stauscode:",req.status_code)
soup=BeautifulSoup(req.content,'html.parser')

title=soup.find('div',{"id": "raa-div-prduct"}).h1.text # .text returns text content
price=soup.find('span',{"id": "price_old"}).text.replace('.00','')
print('product:',title)
print('price:',price)

#to target a class, use 'class_' instead of 'class', since it is a keyword
desc=soup.find('div',class_="styleh2review").text
print(desc)

