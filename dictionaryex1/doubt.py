from task import Task
from logic import addindict,checkTaskid,updatetask

t1=Task(1,"pulkit")
# print(t1)
if checkTaskid(t1.taskid)==True:
    print("Update and delete to be shown")
    updatetask(t1)
else:
    addindict(t1)