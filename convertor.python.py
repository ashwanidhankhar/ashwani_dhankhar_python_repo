#CONVERTER

#enter your height in foot
heightInFoot=input("enter your height in foot >")

#enter you height in inch
heightInInch=input("enter your height in inch  >")

#1 foot = 0.3048m
footIntoMeter=0.3048

#1 inch = 0.0254
inchIntoMeter=0.0254

# formula for converting height in foot/inch into meter
heightIntoMeter=(heightInFoot*footIntoMeter)+(heightInInch*inchIntoMeter)

#
heightIntoCentimeter=heightIntoMeter*100

#printing the result
print (heightIntoMeter)
print (heightIntoCentimeter)
