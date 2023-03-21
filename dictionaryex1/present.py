from logic import updatetask,addindict,checkTaskid,viewTask
from task import Task

def init():
    exit=False
    while exit==False:
        print("-----------Menu-------------")
        print("1.Enter task id\n0.exit")
        cha=int(input("enter your choice:"))
        if cha==1:
            n=int(input("Enter task id"))
            reslt=checkTaskid(n)
            if reslt==True:
                print(f"Taskid {n} is already available available,update it.")
                existTask()
            else:
                print("----------create a new task-------------")
                addtask()
            # else:
            #     print("---ADD A NEW TASK----")
            #     print("1.Enter the task name.\n2.description.\")

            
def existTask():
    print('welcome here')
    exit=False
    while exit==False:
        print("1.Update Task Information\n2.view task information\n3.remove task information.\n4.enter in menu")
        cha=int(input("enter your choice:"))
        if cha==1:
            taskid=int(input("enter taskid for update"))
            taskname=input("update your taskname:")
            describe=input("description for update:")
            priority=int(input("enter priority for update"))
            x=(taskid,taskname,describe,priority)
            t2=Task(taskid,taskname,describe,priority)
            print(t2)
            updatetask(t2)
        if cha==2:
            print("welcome to view")
            taskid=int(input("enter task id:"))
            views=viewTask(taskid)
            print(views)
        if cha==3:
            print("-------remove your task here-------------")
            




        
        else:
            init()

def addtask():
    taskid=int(input("enter task id:"))
    taskname=input("Enter your taskname:")
    describe=input("enter your description:")
    priority=int(input("enter priority:"))
    x=(taskid,taskname,describe,priority)
    result=Task(taskid,taskname,describe,priority)
    print(result)


            




