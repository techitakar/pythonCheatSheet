#Range
range(10) #same as (0,10), which means 0 to 10
list(range(10)) #
l1=list(range(5,20)) #5 to 20
print(l1)
l2=list(range(5,20,2)) #5 to 20 with diffrence of 2
print(l2)

#Bitwise operators
a=5
b=6
print("and:",a&b)
print("or:",a|b)
print("xor:",a^b)
print('complement:',~a)
print("not: ",not(a))

#convert Formats
print(bin(360))#binary
print(oct(360))#octal
print(hex(360))#hex
print(int(0x360))#int

#swap variables
#old Method:
c,d=15,20
print("c:",c,"d:",d)
temp=c
c=d
d=temp
print("After Swap, c:",c,"d:",d)
#cool Method:
c=c+d
d=c-d
c=c-d
print("After Cool Swap, c:",c,"d:",d)