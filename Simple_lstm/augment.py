import random

def augment(x):
    retVal = []
    for val in x:
        retVal.append(val + random.randint(-10,10)/100)
    
    return retVal