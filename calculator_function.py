import math
def add_1 (x,y):
    return(x+y)
def sub_1 (x,y):
    return(x-y)
def mult_1 (x,y):
    return(x*y) 
def    devi_1(x,y) :
    if y==0:
        return 'not accept zero division'
    else:
        return(x/y) 
def    exp_1 (x)  :
    return(math.exp(x))
def cos_1   (x) :
    return(math.cos(x))
def sin_1   (x) :
    return(math.sin(x))
def sqrt_1   (x) :
    if x<0:
        return 'we cant get sqrt for negative parts'
    return(math.sqrt(x)) 
def power_1   (x) :
    return(x**2)       
