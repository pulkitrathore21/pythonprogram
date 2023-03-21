d1={1:(1,"pulkit","rathore",2)}


def updatetask(t2):
    d1[t2.taskid]=t2
    print(d1)


def checkTaskid(n):
    if d1.get(n)!=None:
        return True
    else:
        return False
def addindict(x):
    d1[x.taskid]=x

def viewTask(x):
    return d1.get(x)






