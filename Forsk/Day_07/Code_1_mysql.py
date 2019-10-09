# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 01:38:03 2019

@author: BSDU ADMIN
"""

import mysql.connector




conn = mysql.connector.connect(user='ashwani_dhankhar', password='ashwanidhankhar',
                              host='db4free.net', database = 'db_university201')


c=conn.cursor()


#c.execute('CREATE DATABASE unversity_db')

c.execute('USE db_university201')

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


print ( c.fetchall() )

from pandas import DataFrame

df=DataFrame(c.fetchall())

print(df)