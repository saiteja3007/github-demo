#Add Implementation
def add(x,y):
    return x+y

#Subtract Implementation
def subtract(x,y):
    return x-y              #Main Branch

#Multiply Implementation
def multiply(x,y):
    return x*y              #Bug456 Branch

#Divide Implementation
def divide(x,y):
    if y==0                 #Bug789
        return DIVIDE_BY_0_ERROR
    else
        return x/y