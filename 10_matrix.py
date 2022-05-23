'''
#different methods of importing modules
from numpy import *
from numpy import cos
from numpy import cos,sin
from numpy import cos as cosine
from numpy import cos,sin
'''

from numpy import *
arr1=array([
    [1,2,3,4,5,6],
    [3,4,5,6,7,8]
])
print(arr1.ndim)#no. of dimensions
print(arr1.shape)#no. of rows and columns
print(arr1.size)#rows * colums

arr2=arr1.flatten()#convert from 2d to 1d
print(arr2)
arr3=arr2.reshape(3,4)#convert 1d to 3d, reshape(rows,columns)
arr4=arr2.reshape(2,2,3)#reshape(no of arrays,),(2 2d array,2 1d array,3 values)
print(arr3)
print(arr4)

#matrix
print('\nmatrix:')
m=matrix(arr1)
m2=matrix('1 2 3 4;5 6 1 5')
m3=matrix('1 2 3;4 5 6;7 8 9')
m4=matrix('5 6 7;2 3 1;3 5 7')
print(m,"\n")
print(m2,"\n")
print(m3,"\n")
print(diagonal(m3),"\n")#get diagonal elements
print(m3+m4)
print(m3*m4)
