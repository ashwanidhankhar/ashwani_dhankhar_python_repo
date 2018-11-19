import os
import csv

os.chdir('C:\\Users\\BSDU\\Desktop\\ashwani')
water1=0
water2=0
water3=0
water4=0
water5=0

with open('zoo.csv') as zoo_csv:
    csv_reader=csv.reader(zoo_csv,delimiter=',')
    next(csv_reader)
    split1={}
    for split in csv_reader:
        if(split[0]=='elephant'):
            water1 += int(split[2])
            split1[split[0]]= water1
        elif(split[0]=='tiger'):
            water2 += int(split[2])
            split1[split[0]]= water2
        elif(split[0]=='lion'):
            water3 += int(split[2])
            split1[split[0]]= water3
        elif(split[0]=='kangaroo'):
            water4 += int(split[2])
            split1[split[0]]= water4
        elif(split[0]=='zebra'):
            water5 += int(split[2])
            split1[split[0]]= water5

    for key,value in split1.items():
        print(key,value)
    
print "water need of all animals is :\n",split1
