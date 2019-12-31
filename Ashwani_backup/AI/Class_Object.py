# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:13:47 2019

@author: BSDU ADMIN
"""

class myclass:
    var1=20
    def yoyo():
        print("22")
#object instance from a class    
p1=myclass()
print(p1.var1)

############


#function inside a class
p2=myclass.yoyo()




###############################################################################

class myclass:
    var1=20
    def yoyo(self):
        print("22")
#object instance from a class    
p1=myclass()
print(p1.var1)

############


#function inside a class after self
p1.yoyo()


###############################################################################

class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
obj1=employee("ash",19)
obj2=employee("lavish",21)

print(obj1.age,obj1.name)


###############################################################################


def main():
    print("welcome")
    
if __name__== "__main__":
    main()
    
    
###############################################################################
    
#example
    


class employee:
    def __init__(self,identity=0,name="",salary=0,city="",gender=""):
        self.identity=identity
        self.namer=name
        self.salary=salary
        self.gender=gender
        self.city=city
        
    def getdata(self):
        self.identity=int(input("Enter Employee id :"))
        self.name=input("Enter Employee name :")
        self.salary=int(input("Enter Employee salary :"))
        self.gender=input("Enter Employee gender :")
        self.city=input("Enter Employee city :")
    def showdata(self):
        print("Employee identity :",self.identity)
        print("Employee name :",self.name)
        print("Employee salary :",self.salary)
        print("Employee gender :",self.gender)
        print("Employee city :",self.city)
        
def main():
    #employee object
    emp=employee()
    emp.getdata()
    emp.showdata()
        
if __name__=="__main__":
    main()



















