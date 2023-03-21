import random
from present import*
l1=[]
def appendList():
    for i in range(1,10):
        l1.append(random.randint(0,22))
    return l1
def viewList():
    return l1

def addnumber(num):
    l1.append(num)
    return l1

def sortedlist():
    b=sorted(l1)
    return b
def sortedDesc():
    b=sorted(l1)
    return b[::-1]



