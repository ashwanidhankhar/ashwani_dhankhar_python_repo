#importing the sql library
import sqlite3
import os
import csv

os.chdir("C:\\Users\\BSDU\\Desktop\\ashwani\\python\\db handling\\db for python")

#establishing a connection between the python and db. creating a db.
conn = sqlite3.connect("zoo.db")

#creating the cursor
c = conn.cursor()

#creating a table
#c.execute("""CREATE TABLE zoo(animal TEXT,uniq_id INTEGER,water_need INTEGER)""")

animal="''"
uniq_id=0
water_need=0
cnt = 0

#importing zoo.csv
with open ("zoo.csv")as csv_file:
    #reading each line and storing it in variable
    csv_reader=csv.reader(csv_file,delimiter=',')
    # instead of cnt and using if else we can also set next(csv_reader to skip the first line

    #using for loop to read each line and storing it in row
    for row in csv_reader:
        #to skip the first line
        if cnt ==0:
            cnt = 1
            continue
        else:
            #storing value of column stored in row in defined variables
            animal=row[0]
            uniq_id=row[1]
            water_need=row[2]
            #inserting value row by row in the table
            c.execute("""INSERT INTO zoo VALUES('{}',{},{})""".format(animal,uniq_id,water_need))
        
        

#fetching the value 
c.execute("SELECT * FROM zoo")
print(c.fetchall())


