#binary into decimAL LOGICAL

#
binaryInput= input(" enter the binary number : ")

#
onesDigit=binaryInput%10

#
remainedDigits=binaryInput/10

#
print"ones digit =",onesDigit

#
print"remained digits =",remainedDigits

#
tensDigit=remainedDigits%10

#
remainedDigits=remainedDigits/10

#
print"digit at tens=",tensDigit

#
print"remained digits",remainedDigits

#
hundredsDigit=remainedDigits%10

#
remainedDigits=remainedDigits/10

#
print"digit at hundreds",hundredsDigit

#
print"remainedDigits",remainedDigits


thousandsdigit=remainedDigits%10

#
remainedDigits=remainedDigits/10

print"digit at thousands",thousandsdigit

#
print"remainedDigits",remainedDigits

#
decimal=(onesDigit*(2**0))+ (tensDigit*(2**1))+ (hundredsDigit*(2**2)) +(thousandsdigit*(2**3))

#
print"decimal values=",decimal
