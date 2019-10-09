# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 02:29:02 2019

@author: BSDU ADMIN
"""

import pymongo


client = pymongo.MongoClient("mongodb+srv://ashwanidhankhar:<password>@cluster0-e0jms.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

def add_student(name,age,roll,branch):
    unique_employee = db.students.find_one({"id":idd})
    if unique_employee:
        return "Student already exists"
    else:
        db.students.insert_one(
                {
                "Students_name" : name,
                "age" : age,
                "roll" : roll,
                "branch" : branch
                })
        return "Student added successfully"


def fetch_all_student():
    user = db.students.find()
    for i in user:
        print (i)
        
        
add_student(1,'Sylvester', 'Fernandes', 50000)
add_student(2,'Yogendra', 'Singh', 70000)
add_student(3,'Rohit', 'Mishra', 30000)
add_student(4,'Kunal', 'Vaid', 30000)
add_student(5,'Devendra', 'Shekhawat', 30000)