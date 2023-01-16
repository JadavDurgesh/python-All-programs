"""
function without parameters and function with return type

syntax:

def funname():
    return statement

"""

def checkeligeble(age):

    if age > 18:
        return "eligible for votting"
    else:
        return "not eligible fot votting"

print(checkeligeble(22))