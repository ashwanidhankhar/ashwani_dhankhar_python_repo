
num = int(input("enter a number: "))
sum = 0
while(num > 0):
    sum = num + sum
    num = num - 1
    print("number after decrease",num)
    print("the sum is", sum)
    