'''
Method overloading: In the same class, there can be two methods with the same name that acts differently depending on the no. of arguments
    >def add(x,y)
    >def add(x,y,z)

Method overriding: If a class inherits another class, it can override the methods of the super class with same name and no. of arguments
'''

#method overloading
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m1=m2
    
    def sum(self,x=None,y=None,z=None):
        if x!=None and y!=None and z!=None:
            return x+y+z
        elif x!=None and y!=None:
            return x+y
        else:
            return x

s1=Student(11,3)
print(s1.sum(55,2))
print(s1.sum(33,41,53))

#method overriding
class X:
    def run(self):
        print("running in X...")

class Y(X):
    def run(self): #overriding
        print("running in Y....")

y1=Y()
y1.run()