#if Else
a=41
if a>50:
    print(a,"is greater than 50")
else:
    print(a,"is not greater than 50")

x=2
if x==1:
    print("one")
elif x==2:
    print("two")
elif x==3:
    print("three")
else:
    print("GRAPEEE!!!!")

#While loop
i=1
while i<=5:
    print("currently in ",i)
    i+=1

#nested loop
i=1
while i<=5:
    print("outer loop: ",i)
    j=1
    while j<=5:
        print(":",j,end=" ") #(end=" "), for print on same line
        j+=1
    i+=1
    print("\n")

#For loop, to travarse for loop we need a list for it
x=['goopz',55,True,11.3] #tradional list
for i in x:
    print(i)
y='Oh Hi Mark'
for i in y:
    print('[',i,']',end=",")
print("\n")
for i in range(10): #or we can create a list using range
    print(i,end=",")
print("\n")
for i in range(5,20,2):
    print(i,end=",")
print("\n")
for i in range(20,1,-1): #go in reverse
    print(i,end=",")
print("\n")
for i in range(1,30): 
    if i%2==0:
        print(i,end=",")
print("\n")

#break, continue, pass same as in c