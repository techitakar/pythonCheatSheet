#>pip3 install mysql-connector-python
#pip3 list
#pip3 show mysql-connector-python

import mysql.connector

cnx=mysql.connector.connect(host="localhost",user="goopzz",passwd="toor123",database="movies")
mycursor=cnx.cursor()#cursor are like pointers to database
mycursor.execute("show databases;") #it returns a list of databases

# for i in mycursor:
#     print(i)

result=mycursor.fetchall() #can also use fetchone()
for i in result:
    print(i)
