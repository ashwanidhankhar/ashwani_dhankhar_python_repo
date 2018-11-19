#decimal to binary conversion (wrong logic)

# storing the binary number
binary= input("enter the binary number  >")

'''
#separating the value of once place
decimalOnes = binary%10/1

#separating the value of tens place
decimalTens= binary%100/10

#separating the value of hundreds place
decimalHundreds=binary%1000/100

#separating the value of thousands place
decimalThousands=binary%10000/1000'''

lst = []
i = 0
while i < len(str(binary)):
    div1 =  int("10"+i*"0")
    div2 =  int("1"+i*"0")
    decimalOnes = binary%div1/div2
    lst.append((decimalOnes)*(2**i))
    i += 1
    
    

#formula for calculating binary into decimal = 2 power n wehre n belongs 0 to infinty         
#decimal5=((decimalOnes)*(2**0))+((decimalTens)*(2**1))+((decimalHundreds)*(2**2))+((decimalThousands)*(2**3))
decimal5 = sum(lst)

#printing the result
print(decimal5)
++
+
