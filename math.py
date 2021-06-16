#Add Implementation
def add(x,y):
    return x+y

#Subtract Implementation
def subtract(x,y):
    return x-y          #master

#Multiply Implementation
def multiply(x,y):
    return x*y          #Bug456 branch

#Divide Implementation
def divide(x,y):
    if x<0:
        return NEGATIVE_PARAM_ERROR     #on master branch
    if y==0:  
        return DIVIDE_BY_0_ERROR     #Bug789
    else:
        return x/y
        
def square(x):
    return x*x