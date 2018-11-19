#printing age using if else and elif statements

age=input("enter you age :")

if(age>0 and age<=1):
    print(u"infant 👶")
elif(age>1 and age<=12):
    print(u"child 👦")
elif(age>12 and age<18):
    print(u"teenager 👦")
elif(age>=18 and age<60):
    print(u"Adult 👨")
elif(age>=60 and age<120):
    print(u"senior citizen 👴")
elif(age>=120):
    print(u" You are a ghost 👻 ")
else:
    print (u"entered invalid age ❌ ⚠️")
    
    
