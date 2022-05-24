#Abstract class has only declaration but no definition of methods
#python doesn't support abstract classes by default, we need abc module, abc=abstract based classes

from abc import ABC, abstractmethod

#abstract class has all methods name but are not defined
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self): # we need to compulsoraily define this method
        print("process running....") 

com1=Laptop()
com1.process()

'''
use eg: suppose we built an api, we can create an abstract class with methods such as request(), response(), exit() and not define any of them...
now if someone creates classes extending to our abstract class, they have to define those methods 
'''