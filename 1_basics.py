#basics
name="Gandalf"
print(name,"rocks!!")
print("4th letter is ", name[3])
sent="May the force be with you..."
print(sent[1:10])
print(sent[5:])
print(sent[:9])

#modules
print(help('LISTS')) #info about lists
print(help('modules')) #list of all modules available

#basic functions
print(type(name))
print(id(name)) #address of name
print(hex(id(name))) #address in hex

#lists
nums=[53,231,532,332,1,5,88]
# print(nums[5])
names=['solo','luke','anakin','Obi wan','padme']
print(names[3])


#lists functions
print(nums)
nums.append(33) #add to last
print(nums,"33 added to last")
nums.clear()#clears the list
print(nums,"list cleared")
nums=[53,231,3,532,332,3,1,5,88]
print("occurance of 3 is ",nums.count(3)) #count the occurance of 3
nums.extend([534,33,13,53]) #add these values to nums
print(nums,"new list")
print("332 is located in index ",nums.index(332)) #index of 332
nums.insert(2,69) #insert value 69 at index 2
nums.pop() #remove last element
nums.remove(332) #remove 332
print("list after above changes",nums)
nums.reverse() #reverse the list
print("list after reverse",nums)
nums.pop(4) #remove element at index 4
print(nums)
del nums[4:] #delete from index 4 and so on
print("list values after removal of index 4 and above",nums)
nums.extend([54,321,76,54])
print("length of nums:",len(nums))
print("minimum in the list",min(nums))
print("maximum in the list",max(nums))
print("sum of  the list",sum(nums))
print("original order",nums)
nums.sort()
print("after sort",nums)

gpd=[9.5,True,"Harley"] #list can have different datatypes and are mutable unlike strings

