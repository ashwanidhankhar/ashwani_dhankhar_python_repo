#importing the sql library
import sqlite3
import os
import csv



os.chdir("C:\\Users\\BSDU\\Desktop\\ashwani\\python\\db handling\\db for python")
check=os.listdir("C:\\Users\\BSDU\\Desktop\\ashwani\\python\\db handling\\db for python")
print check



while(True):
    print ("Press 1 to import zoo.csv")
    print ("Press 2 to import students.csv")
    print ("Press 3 to import carmakers.csv" )
    print ("Press 4 to exit the program \n")

    
    csv_name=input("enter the CSV number :")
    
    def create_database(database_name):
        #establishing a connection between the python and db. creating a db.
        conn = sqlite3.connect(database_name)

        #creating the cursor
        c = conn.cursor()
        return c
        


    if(csv_name==1):
        #creating database
        c = create_database("zoo.db")

        
        #creating a table
        #c.execute("""CREATE TABLE zoo(animal TEXT,uniq_id INTEGER,water_need INTEGER)""")

        animal="''"
        uniq_id=0
        water_need=0
        cnt = 0

            #importing zoo.csvreader
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
        print("\n")

    elif (csv_name==2):
         #creating database
        c = create_database("students.db")
        

        #creating a table
        #c.execute("""CREATE TABLE students(lastName TEXT,firstname TEXT,grade INTEGER,classroom INTEGER)""")
        
        lastName="''"
        firstname="''"
        grade=0
        classroom=0
        cnt = 0

            #importing students.csv
        with open ("students.csv")as csv_file:
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
                    lastName=row[0]
                    firstname=row[1]
                    grade=row[2]
                    classroom=row[3]
                    #inserting value row by row in the table
                    c.execute("""INSERT INTO students VALUES('{}','{}',{},{})""".format(lastName,firstname,grade,classroom))
                
                

        #fetching the value 
        c.execute("SELECT * FROM students")
        print(c.fetchall())
        print("\n")

    elif (csv_name==3):
         #creating database
        c = create_database("carmakers.db")
        

        #creating a table
        #c.execute("""CREATE TABLE cars(makers TEXT,fullname TEXT,country INTEGER)""")
        
        makers="''"
        fullname="''"
        country=0

        cnt = 0

            #importing carmakers.csv
        with open ("carmakers.csv")as csv_file:
            #reading each line and storing it in variable
            csv_reader=csv.reader(csv_file,delimiter=';')
            # instead of cnt and using if else we can also set next(csv_reader to skip the first line

            #using for loop to read each line and storing it in row
            for row in csv_reader:
                #to skip the first line
                if cnt ==0:
                    cnt = 1
                    continue
                else:
                    #storing value of column stored in row in defined variables
                    makers=row[0]
                    fullname=row[1]
                    country=row[2]
                    #inserting value row by row in the table
                    c.execute("""INSERT INTO cars VALUES('{}','{}',{})""".format(makers,fullname,country))
                
                

        #fetching the value 
        c.execute("SELECT * FROM cars")
        print(c.fetchall())
        print("\n")
        
    elif(csv_name==4):
        print("\n You Ended the program")
        break
        
    else:
        print("Please enter a valid csv number")
        print("\n")




