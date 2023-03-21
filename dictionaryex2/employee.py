
class Emp:
    def __init__(self,empno,empname,age,depid):
        self.empno=empno
        self.empname=empname
        self.age=age
        self.depid=depid

    def __str__(self):
        return f"{self.empno},{self.empname},{self.depid},{self.age}"
    
class EmpStatus():
    def __init__(self,statuscode,message,employeobj):
        self.statuscode=statuscode
        self.message=message
        self.employeobj=employeobj
    


