"""
tuple as a parameter 


and 

dectionary as a parameter 


----------------------------

*args & **kwargs


args : arguments
kwargs : key with arguments



"""

# normal function

def fun(num1,num2,num3):
    sum = num1+num2+num3
    print(sum)

fun(12, 25, 33)

# args : tuple as a parameter - we can pass no of parameter

def my_fun(*args):
    sum= 0
    
    for i in args:
        sum+=i
    print(sum)
my_fun(12,50,30,54)