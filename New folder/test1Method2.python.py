
#this program prints even numbers from a given numbers list in the same order and stops the printing if any number that comes after 237 in the sequence(no user input required)

a=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,
   67,104,58,512,892,767,553,81,379,843,831,445,742,717,958,743,527]

# here initialization point is i which is 0. now loop starts a index i where i is zero till a not equals to 237.
i = 0
while(a[i] != 237):
    #if index of a which is "i" is divisible by 2 it will print the number  
    if(a[i]%2==0):
        print a[i]

    #every time  value of i which is currently 0 will increase by 1.    
    i = i + 1
