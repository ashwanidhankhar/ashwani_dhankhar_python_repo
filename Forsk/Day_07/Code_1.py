# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:22:10 2019

@author: BSDU ADMIN
"""


"""
Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like Student_Name, Student_Age, 
Student_Roll_no, Student_Branch.
"""

import sqlite3

conn=sqlite3.connect('db_university')

c=conn.cursor()

#c.execute("DROP TABLE students")

c.execute("""create table students(
        Students_Name TEXT,
        Students_Age INTEGER,
        Student_Roll_no INTEGER,
        Student_Branch TEXT)""")
conn.commit()


c.execute("INSERT INTO students VALUES('Ashwani',19,005,'ML/AI')")

c.execute("INSERT INTO students VALUES('Ankit',19,003,'ML/AI')")

c.execute("INSERT INTO students VALUES('Lavish',18,006,'ML/AI')")

c.execute("INSERT INTO students VALUES('Vishal',19,007,'ML/AI')")

c.execute("INSERT INTO students VALUES('Lokesh',20,008,'ML/AI')")

c.execute("INSERT INTO students VALUES('Nishu',19,009,'ML/AI')")

c.execute("INSERT INTO students VALUES('Lakshay',19,012,'ML/AI')")

c.execute("INSERT INTO students VALUES('Shubham',18,032,'ML/AI')")

c.execute("INSERT INTO students VALUES('Dinesh',19,043,'ML/AI')")

c.execute("INSERT INTO students VALUES('Chandu',19,041,'ML/AI')")

conn.commit()


c.execute("SELECT * FROM students")
conn.commit()

print ( c.fetchall() )

