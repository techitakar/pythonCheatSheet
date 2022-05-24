#Object oriented programming
class Npc:
    def talk(self):
        print("I was an adventurer like you, then i took an arrow to the knee")

guard=Npc()
guard.talk() #talk will take guard as an argument, hence self at line 2 

#class will constructor(__init__)
class Game:
    def __init__(self,title,year):
        self.title=title #self is the object, so it can be seen as ac2.title=title
        self.year=year
        
    def desc(self):
        print(self.title, "was released in ",self.year)

ac2=Game('Assassins creed 2',2009) #we are actually passing 3 arguments, title,year and self, i.e. ac2(the object itself), which is passed automatically
ac2.desc() 

#Instance, Class and static Methods
class Pc:

    company='MSI' #class variable

    def __init__(self,pcr,ram1,ram2):
        self.pcr=pcr #instance variable
        self.ram1=ram1
        self.ram2=ram2
    
    def totalRam(self): #instance method, which works with instance variables
        print("Total ram is ",self.ram1+self.ram2,"gb")

    @classmethod 
    def getCompany(cls): #class method, which works with class variables
        return cls.company

    @staticmethod
    def info(): #static method, has nothing to do with the class variables
        print("Info not found yet....")

    #getters and setters
    def get_ram1(self): #usually the function is called get_ and set_
        return self.ram1

    def set_ram1(self,value):
        self.ram1=value

pc1=Pc('ryzen 5',16,16)
pc2=Pc('i5 9th gen',8,8)
pc2.totalRam()
pc2.set_ram1(64)
print(Pc.getCompany())

#inner class, class inside a class
class Employee: #outer class
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.lap=self.Laptop() #initializing the inner class

    def show(self):
        print(self.name,"id:",self.id)

    class Laptop: #inner class
        def __init__(self):
            self.brand='MSI'
            self.cpu='i7'
            self.ram=8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)
            
emp1=Employee('John',33)
emp1.show()
print(emp1.lap.brand)

lap1=Employee.Laptop()
lap1.show()