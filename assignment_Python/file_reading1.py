import os
import csv

os.chdir("F:\\PYTHON")
water1=0
water2=0
water3=0
water4=0
water5=0
"""

zoo = open('zoo.csv','rt')
zoo_file= zoo.readlines()
for i in zoo_file:
    split=i.split(',')
    if(split[0]=='elephant'):
        water1 += int(split[2])
    elif(split[0]=='tiger'):
        water2 += int(split[2])
    elif(split[0]=='lion'):
        water3 += int(split[2])
    elif(split[0]=='kangaroo'):
        water4 += int(split[2])
    elif(split[0]=='zebra'):
        water5 += int(split[2])


print ( "water consumption of all elephants is:  {} L".format(water1))
print ( "water consumption of all tiger is:      {} L".format(water2))
print ( "water consumption of all lion is:       {} L".format(water3))
print ( "water consumption of all kangaroo is:   {} L".format(water4))
print ( "water consumption of all zebra is:      {} L".format(water5))



"""

                               #OR



with open('zoo.csv') as zoo_csv:
    csv_reader=csv.reader(zoo_csv,delimiter=',')
    for split in csv_reader:
        if(split[0]=='elephant'):
            water1 += int(split[2])
        elif(split[0]=='tiger'):
            water2 += int(split[2])
        elif(split[0]=='lion'):
            water3 += int(split[2])
        elif(split[0]=='kangaroo'):
            water4 += int(split[2])
        elif(split[0]=='zebra'):
            water5 += int(split[2])


print ( "water consumption of all elephants is:  {} L".format(water1))
print ( "water consumption of all tiger is:      {} L".format(water2))
print ( "water consumption of all lion is:       {} L".format(water3))
print ( "water consumption of all kangaroo is:   {} L".format(water4))
print ( "water consumption of all zebra is:      {} L \n".format(water5))
        
print ( "Total water consumed by all the animals if {} L").format(water1+water2+water3+water4+water5)

