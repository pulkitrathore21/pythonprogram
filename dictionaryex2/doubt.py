from employee import Emp,EmpStatus
# e1=Emp(1,"pulkit",1001)
# print(e1)
# d1={e1.empno:e1}
# v=d1.get(e1.empno)
# print(v)

x=Emp(1,"pul",24,2)
s=EmpStatus(0,"hii",x)
print(s.statuscode)