
def add(x,y):
    c=x+y
    print("The sum is",c)
def multiply(x,y):
    return x*y
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
add(5,10)
print("Multiple for 6 and 7 is",multiply(6,7))
result1,result2=add_sub(5,4)
print(result1,result2)

'''
#in pass by value when you change the value in a function, it will not affect the original value 
#in pass by reference when you change the value in a function, it will affect the original value as well

def update(x):
    x=10
    print("inside function\naddress of x is",hex(id(x)),"\nand its value is ",x)
a=20
print("outside function\naddress of a is",hex(id(a)))
update(a)
print("value of a is ",a)
'''

'''
    Type of arguments:
        -keyword arguments
        -default arguments
        -variable length
'''

def person(name,age):
    print(name)
    print(age)

person('goopzz',23)
person(age=35,name='Ben')#keyword arguments

def person2(age=18): #default value
    print(age)
person2(32) #overriding

def sum(a,*b):# variable length, *b means it can have multiple values and is a tuple
    c=a
    for i in b:
        c+=i
    print(c)
sum(5,6,63,44) # a=5,b=(6,63,44)

#keyword variable length argument
def person3(name, **data):# **data means a key value pair argument
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person3('goopz',age=23,city='LA',num=433244)

#global and local variable
a=10
print(id(a))
def something():
    a=9 #local variable
    x=globals()['a'] #u can access any global variables using this function
    print(id(x))
    print("in fun ",a)
    globals()['a']=15 #change global variable
something()
print("outside",a)