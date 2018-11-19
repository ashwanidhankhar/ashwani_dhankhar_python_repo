# average caluclator on miles/gallon

# storing the distance travelled 
distanceTravelled= input("enter distance travelled in kilometers  >")

#storing value of fuel consumed during trip
fuelConsumption= input(" enter the amount of fuel consumed in litres   >")

#conversion of km in miles
kmIntoMiles=0.621371

#conversion of litres into gallon
litresIntoGallon=0.264172

#average of vehicle in miles/gallon
average=(float(distanceTravelled)*kmIntoMiles)/(float(fuelConsumption)*litresIntoGallon)

#result
print(average)
