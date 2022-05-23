def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def pt():
    print(__name__)
pt()
if(__name__) == '__main__': #will run only if this is the main file; if it is imported as a module, it will not run
    print("I am the main character")