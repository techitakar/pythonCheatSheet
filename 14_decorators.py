def div(a,b):
    return a/b
#suppose we input (2,4) instead of (4,2), we just need a check condition, but if we dont have access to the function we use decorators

def smart_div(func): #we pass a function as an argument
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

new_div=smart_div(div) #new_div is the funtion
print(new_div(4,2))