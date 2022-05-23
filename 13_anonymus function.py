import random
from functools import reduce
def square(a):
    return a*a
print(square(5))

sqr=lambda y:y*y #lambda function used for single expression functions
add=lambda a,b:a+b
print(sqr(6))
print(add(44,5))

#filter(),map() and reduce()
nums=[]
for i in range(10):
    nums.append(random.randint(1,30))
print(nums)

#filter
evens=list(filter(lambda n:n%2==0,nums))#filter based on a funtion, filter(function,list)
print(evens)

#map
doubles=list(map(lambda n:n*2,evens))#map takes two arguments, map(function,list)
print(doubles)

#reduce
sum=reduce(lambda a,b:a+b,doubles)
print(sum)
