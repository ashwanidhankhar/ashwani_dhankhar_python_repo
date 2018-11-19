zoo_file = open("zoo.csv","rt")

read_file = zoo_file.readlines()


water = 0
for i in read_file:
    split = i.split(",")
    if split[0]=="water_need":
         
