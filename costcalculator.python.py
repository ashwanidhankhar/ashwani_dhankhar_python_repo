#cost of travel calculator

#enter present cost of fuel
costOfFuel=input("enter the cost of fuel >")

# enter distance to be travveled
distanceTravelled=input("enter distance to be travelled  >")

#eneter the average of the vehicle in which travelling
average=input(" enter the average of vehicle  >")

#enter the no. of person traveeling in the vehicle
peopleTravelling=input(" enter the number of people travelling >")

#formula for fuel consupmtion in 1 km = distance travelled/average of the vehicle
fuelInDistanceTravelled=distanceTravelled/float(average)

#formula for total cost of the travel=fuel consumption in 1km/present fuel cost 
costForTravel=fuelInDistanceTravelled*costOfFuel

#formula for spliting fuel cost into members
shareTheBill=costForTravel/peopleTravelling

#printing the result
print (costForTravel)
print (shareTheBill)
