"""
function with return type and function with paramrters :

def funname(paremeters):
    return types


"""


def simoleinterest(p,r,n):
    si = p*n*r/100

    return si

p = int(input("enter the prriciple amout :"))
n = int(input("enter the no. of terms :")) 
r = int(input("enter the  rate :"))


print(simoleinterest(p, r, n))