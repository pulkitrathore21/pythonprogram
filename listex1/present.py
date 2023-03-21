
from logic import appendList,viewList,l1,addnumber,sortedlist,sortedDesc


def init():
    exit=False
    while exit==False:
        print("1.list with 10 random numbers.\n2.view the list.\n3.change the number in list.\n4.remove element in list.\n5. sort the array.\n6.sorted in descending order.\n0.exit.")
        cha=int(input("choose a number:"))
        if cha==1:
            r=appendList()
            print(r)
        elif cha==2:
            r=viewList()
            print(r)
        elif cha==3:
            num=int(input("enter a number to change:"))
            if num in l1:
                print("this number is already exist")
            else:
                r=addnumber(num)
                print(r)

        elif cha==4:
            num=int(input("enter number to remove"))
            l1.remove(num)
            print("number deleted successfully")
        elif cha==5:
            r=sortedlist()
            print(r)

        elif cha==6:
            r=sortedDesc()
            print(r)
        elif cha==0:
            exit=True

