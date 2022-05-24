#first we sort the list, split it in half, search each half and discard if not found and go on 
from random import randint

pos=0
nums=[]
for i in range(10):
    nums.append(randint(1,30))

def binSearch(list,n):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list[mid] < n:
            low = mid + 1
 
        elif list[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1
 
 
print(nums)
n=int(input("Enter a no. to search: "))
if binSearch(nums,n):
    print("Found at position")
else:
    print("Not Found!!.....")