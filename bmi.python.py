#bmi

#storing my weight in kg
myWeight=75

#storing my height in foot
myHeightInFoot=5

#storing my height in inch
myHeightInInch=10 

# 1 foot = 0.3048m
footIntoMeter=0.3048 

# 1 inch = 0.0254m
inchInMeter=0.0254 

#formula for converting height from foot into meter
myHeightInMeter=(myHeightInFoot*footIntoMeter)+(myHeightInInch*inchInMeter)

#formula for calculating bmi
myBmi=(myWeight)/(myHeightInMeter)**2  

#printing my bmi
print myBmi 
print myHeightInMeter


