#decimal to binary conversion (wrong logic)

# storing the binary number
binary= input("enter the binary number  >")

#separating the value of once place
decimalOnes = binary%10/1

#separating the value of tens place
decimalTens= binary%100/10

#separating the value of hundreds place
decimalHundreds=binary%1000/100

#separating the value of thousands place
decimalThousands=binary%10000/1000

#formula for calculating binary into decimal = 2 power n wehre n belongs 0 to infinty         
decimal5=((decimalOnes)*(2**0))+((decimalTens)*(2**1))+((decimalHundreds)*(2**2))+((decimalThousands)*(2**3))

#printing the result
print(decimal5)
