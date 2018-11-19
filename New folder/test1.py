

#this program prints even numbers from a given numbers list in the same order and stops the printing if any number that comes after 237 in the sequence(no user input required)

a=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,
   67,104,58,512,892,767,553,81,379,843,831,445,742,717,958,743,527]

#for each element of a in a if divisible by 2 it will print the number and if element in a = 237 it will break the program 
for a in a:
    if(a%2==0):
        print a
    elif(a==237):
        break
