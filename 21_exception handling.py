'''
Types of errors:
    1)Compile time Error: missing colon(:)
    2)Logical Error: Gives wrong output(2+2=5)
    3)Run Time Error: Normal execution works fine but wont work for specific inputs(6/0)
'''
a,b=5,2
try:
    print(a/b)
except Exception:
    print("Cant divide a no by zero...")

list=[21,35]
try:
    print(list[2])
except Exception as e:
    print("Error...",e)

#we have different exception for different errors
try:
    print('resource open....')
    print(a/b)
    k=int(input("Enter a number:"))
    print(k)
except ZeroDivisionError as e:
    print("Cant divide a no by zero...")
except ValueError:
    print("Only number allowed....")
except Exception:
    print("Something went wrong.....")
finally: #it will execute eitherway
    print('resource closed....')
