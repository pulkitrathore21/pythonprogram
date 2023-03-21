from dicpresent import*

d1={}

def checkWord(word):
    if d1.get(word)!=None:
        d1[word]+=1
        return True
    else:
        addword(word)
        


def addword(word):
    d1[word]=1
    return d1

def viewWord():
    l1=[]
    for i in d1.keys():
            l1.append(i)
    return l1

def WordWithOcc():
    l2=[]
    for i,j in d1.items():
        l2.append((i,j))
    return l2



