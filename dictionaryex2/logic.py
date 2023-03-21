
from employee import Emp,EmpStatus
emp1=Emp(1,"raj",23,1)
emp2=Emp(2,"raghu",25,1)
emp3=Emp(3,"ram",22,2)
emp4=Emp(4,"latha",21,2)
emp5=Emp(5,"Reshma",22,3)

d={emp1.empno:emp1,emp2.empno:emp2,emp3.empno:emp3,emp4.empno:emp4,emp5.empno:emp5}

def getemp(x):
    try:
        print(d[x])
        return d[x]
    except:
            return "No such ID"


def getsamedpt(x):
    l=[]
    for i in d.values():
        if i.depid==x:
            l.append(i.empname)    
    return l

def statuscheck(x):
     if d[x]!=None:
        print(d[x])
        return EmpStatus(1,"got result",d[x])
     
     else:
          return EmpStatus(0,"not found",'none')
            

