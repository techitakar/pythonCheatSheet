#search element in a list
from random import randint

pos=1
def search(list,n):
    for i in list:
        if i==n:
            return True
            break
        globals()['pos']+=1

    return False

nums=[]
for i in range(10):
    nums.append(randint(1,30))

print(nums)
n=int(input("Enter a no. to search: "))
if search(nums,n):
    print("Found at position",pos)
else:
    print("Not Found!!.....")