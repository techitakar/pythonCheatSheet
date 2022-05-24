#read mode
f=open('./files/sw.txt','r')
# print(f.read())#print entire file
print(f.readline()) #read one line
print(f.readline())
print(f.readline(4)) #print 4 characters

#write mode
f1=open('./files/sw2.txt','w')#create a file if it doesnt exist
f1.write("Hello There")
f1.write('\nGeneral Kenobiii')

#append mode
f2=open('./files/sw2.txt','a')
f2.write("\nA surprise to be sure, but a welcome one")

for data in f:
    print(data)

for data in f:
    f1.write(data) #read from sw.txt and write to sw2.txt

#image data
p1=open('./files/samurai.jpg','rb') #read binary
#print(p1.read())

#create new jpg
p2=open('./files/newPic.jpg','wb')
for i in p1:
    p2.write(i)