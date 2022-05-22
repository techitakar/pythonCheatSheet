#lists != arrays
import array as arr
vals=arr.array('i',[2,32,41,53,43,32,43]) #array(type,values)
#type i:int signed, I:int unsigned, b:signed char, B:unsigned char, f:float, d:double
print(vals)
print("typecode is",vals.typecode)
print(vals[2])
print(vals.buffer_info()) #(address,size)
print(hex(vals.buffer_info()[0])) #address in hex
vals.reverse()
print(vals)

for i in range(len(vals)):
    print(vals[i],end=",")
print("\n")

valC=arr.array('u',['a','e','i','o','u'])

#creating new array
newArr=arr.array(vals.typecode,(a for a in vals)) #assign a for each a 
print(newArr)
newArr=arr.array(vals.typecode,(a+1 for a in vals)) #assign a+1 for each a 
print(newArr)

#user created array
userArr=arr.array('i',[])#create empty array
n=int(input("Enter length of array:"))
for i in range(n):
    x=int(input("Enter the value:"))
    userArr.append(x)
print(userArr)

