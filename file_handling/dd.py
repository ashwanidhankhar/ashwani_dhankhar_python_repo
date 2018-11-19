#drank by zebra

zoo_file = open("zoo.csv",'rt')

read_file = zoo_file.readlines()

water = 0

for i in read_file:
    split= i.split(',')
    if(split[0]=='zebra'):
        water = water + int(split[2])

print 'total water drank by zebra is=',water

zoo_file.close()
