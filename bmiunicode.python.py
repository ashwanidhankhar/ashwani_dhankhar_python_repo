#bmi using unicode and printing formating
#
name=raw_input(u"\u0905\u092A\u0928\u093E \u0928\u093E\u092E \u0921\u093E\u0932\u093F\u090F  >")

#enter your height in foot
heightInFoot=input(u"\u0905\u092A\u0928\u0940 \u0932\u092E\u092C\u093E\u0908 \u092B\u0941\u091F \u092E\u0947 \u0921\u093E\u0932\u093F\u090F >")

#enter your height in inch
heightInInch=input( u"\u0905\u092A\u0928\u0940 \u0932\u092E\u092C\u093E\u0908 \u0907\u093A\u091A \u092E\u0947 \u0921\u093E\u0932\u093F\u090F>")

#enter your weight in kilograms
weight=input( u"\u0905\u092A\u0928\u093E \u0935\u091C\u093C\u0928 \u0921\u093E\u0932\u093F\u090F >")

#1 foot = 0.3048m
footIntoMeter=0.3048

#1 inch = 0.0254
inchIntoMeter=0.0254

# formula for converting height in foot/inch into meter
heightIntoMeter=(heightInFoot*footIntoMeter)+(heightInInch*inchIntoMeter)

#formula for calculating bmi
bmi=(weight)/(heightIntoMeter)**2

#printing the result
print (u"\u0928\u092e\u0938\u094d\u0924\u0947 {}, your height {}m, and your weight is {}kg,and your BMI is {}.".format(name,heightIntoMeter,weight,bmi))
