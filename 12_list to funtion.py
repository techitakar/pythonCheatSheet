def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

list=[12,43,5,66,23,16,34,56,11]
even,odd=count(list)
print("Even :{} and odd :{}".format(even,odd))#thats new

#fibonacci series
def fibbonaci(x):
    a=0
    b=1
    print(a,end=",")
    print(b,end=",")
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=",")
    print("\n")
# n=int(input("Enter which no. for fibonacci:"))
n=10
fibbonaci(n)

#factorial
def factorial(y):
    f=1
    for i in range(1,y+1):
        f=f*i
    return f
m=5
print(factorial(5))

#recursion
def recFact(n):
    if n==1:
        print(n)
        return 1
    return(recFact(n-1)*n)
print(recFact(5))
    