# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:38:41 2019

@author: ashwa
"""

"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
"""    

#distance travelled in a day
distance=80

#cost of fuel
cost=80

#average if the vehicle 
average=18

#fuel consumption in a day
fuel_consumption=distance/average

#cost of travelling in a day

total_cost=fuel_consumption*cost

#printing the total cost
print("Total cost for driving per day to office is {} INR".format(total_cost/2))