'''
BubbleSort:
compare [0][1], if greater, swap
compare [1][2], if greater, swap
compare [2][3], if greater, swap
compare [3][4], if greater, swap, and so on....
'''

from random import randint

nums=[]
for i in range(10):
    nums.append(randint(1,30))

def bSort(list):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

print(nums)
bSort(nums)
print(nums)

'''
SelectionSort:
compare [0] with [1][2][3]...[len], keep smallest in [0]
start from [1] and compare [1] with [2][3][4]...[len], keep smallest in [1]
and so on....
'''
nums2=[]
for i in range(10):
    nums2.append(randint(1,30))

def selSort(list):
    for i in range(len(list)):
        sm=i
        for j in range(i,len(list)):
            if list[j] < list[sm]:
                list[sm],list[j]=list[j],list[sm]

print(nums2)
selSort(nums2)
print(nums2)