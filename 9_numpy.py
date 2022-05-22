from numpy import *
arr=array([1,2,3,4,5])
arr2=array([2,3,1,5,7],float)
print(arr)
print(arr.dtype)
print(arr2.dtype)
arr3=linspace(0,15,16)#linspace(from,to,break into no of paths) 
arr4=linspace(1,60,20)#linspace(from 0, to 15,break into 20 paths) 
print(arr4)
arr5=arange(1,20,3)#a range, basically range for arrays
print(arr5)

arr6=array([1,2,3,4,5])
arr7=array([2,3,4,5,6])
arr8=arr6 + arr7
print("sum is",arr8)

#numpy functions
n=56
print(cos(n))
print(sin(n))
print(log(n))
print(sqrt(n))
print(sum(arr7))
print(min(arr7))
print(max(arr7))
print(concatenate([arr6,arr7]))