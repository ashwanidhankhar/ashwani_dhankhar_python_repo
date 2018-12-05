num=input("Enter the number")
n=0
x=range(2,9) 
for i in x:
    if(i==num):
        continue
    if(num % i)==0:
        print("Not a prime number")
        break
else:
    print'A prime number'
    

