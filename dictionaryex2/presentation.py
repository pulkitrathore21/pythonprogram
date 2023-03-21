from employee import Emp
from logic import getemp,getsamedpt,statuscheck
def init():
    print("-------MENU---------")
    exit=False
    while exit==False:
        print("1.for employee detail\n2.same department employees\n3.statuscheck.\n0.exit")
        cha=int(input("enter your choice:"))
        if cha==1:
            
            empno=int(input("enter emp no:"))
            result=getemp(empno)
            print(result)
       
        if cha==2:
            depid=int(input("enter dept no:"))
            result=getsamedpt(depid)
            for i in result:
                print(i)

        if cha==3:
            empno=int(input("enter emp no:"))
            result=statuscheck(empno)
            if result.statuscode==0:
                print("emp no not found")
            else:
                print(result.employeobj)


        if cha==5:
            exit=True
