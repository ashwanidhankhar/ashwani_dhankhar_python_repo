#bmi

#enter your height in foot
heightInFoot=input("enter your height in foot >")

#enter your height in inch
heightInInch=input("enter your height in inch  >")

#enter your weight in kilograms
weight=input("enter your weight in kg  >")

#1 foot = 0.3048m
footIntoMeter=0.3048

#1 inch = 0.0254
inchIntoMeter=0.0254

# formula for converting height in foot/inch into meter
heightIntoMeter=(heightInFoot*footIntoMeter)+(heightInInch*inchIntoMeter)

#formula for calculating bmi
bmi=(weight)/(heightIntoMeter)**2

#printing the result
print ("Your BMI = {}".format(bmi))
