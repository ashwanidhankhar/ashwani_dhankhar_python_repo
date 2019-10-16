def func():
    list1 = list()
    while (True):
        user = input("Enter your name : ")
        if user.lower() == 'no':
            break
        list1.append(user)
    print(list1)
func()


def fibo():
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(0,10):
        c=a+b
        a=b
        b=c
        print(c)
fibo()