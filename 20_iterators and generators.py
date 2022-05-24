nums=[35,14,51,75]

itr=iter(nums)#iter object, it saves its last index value
print(itr.__next__())
print(itr.__next__())
print(next(itr))

#to create own iterator, 1)iter 2)next
#iter gives the object of iterator and next gives the next object
class TenValues:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val=self.num
            self.num +=1
            return val
        else:
            raise StopIteration

values=TenValues()
print("self created iter:")
print(values.__next__())
print(values.__next__())

#Generators
def topTen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

values2=topTen()
print("self created iter:")
print(values2.__next__())
print(values2.__next__())
for i in values2:
    print(i)