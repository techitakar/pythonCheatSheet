#inheritance
#can be called parent-child, superclass-subclass
class A: #super class
    def fun1(self):
        print('fun1 started.....')

    def fun2(self):
        print('fun2 started....')

class B(A): #sub class
    def fun3(self):
        print('fun3 started....')
    def fun4(self):
        print('fun4 started....')

class C(B): 
    def fun5(self):
        print('fun5 started.....')

a1=A()
a1.fun1()

b1=B()
b1.fun3()
b1.fun2()#can use method  of A

c1=C()
c1.fun1()#can use method of A and B

#inheritance constructor
class X:
    def __init__(self):
        print("Init of X")

class Y(X):
    def __init__(self):
        super().__init__() #super is reffering to superclass
        print("Init of Y")

y=Y() #if it has no init, it will call init of parent class X



#polymorphism: objects behave differently depending on the situation
# 1)Duck Typing:
class Add:
    def execute(self):
        print('Adding, A+B')

class Subtract:
    def execute(self):
        print('Subtracting, A-B')

class Laptop:
    def operate(self,operation):
        operation.execute()

operation1=Add()
operation2=Subtract()

lap1=Laptop()
lap1.operate(operation1)
lap1.operate(operation2) #for different input, the code function will perform different functions

# 2)Operator Overloading:
n1,n2=5,6
print(n1+n2)
print(int.__add__(n1,n2)) #for '+' __add__ is called, for '*' __mul__ is called
print(n1) #for 'print' it is actually print(n1.__str__())

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other): #overload normal '+' with own function
        m1=self.m1+other.m1 #self=s1, other=s2; m1=s1.m1+s2.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2) #create new object s3
        return s3
    
    def __gt__(self,other): #overload '>' with own function
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self): #overload print with own method
        return '{} {}' .format(self.m1, self.m2)

s1=Student(55,66)
s2=Student(10,30)

total=s1+s2 # '+' changed Student.__add__(s1,s2)
print(total.m1)

if s1>s2: # '>' changed Student.__gt__(s1,s2)
    print("s1 wins")
else:
    print("s2 wins")

print(s1) # 'print' changed Student.__str__(s1)