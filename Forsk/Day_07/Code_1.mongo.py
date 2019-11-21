# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 02:29:02 2019

@author: BSDU ADMIN
"""

import pymongo






client = pymongo.MongoClient("mongodb://ashwanidhankhar:%40Ashwani@cluster1-shard-00-00-e0jms.mongodb.net:27017,cluster1-shard-00-01-e0jms.mongodb.net:27017,cluster1-shard-00-02-e0jms.mongodb.net:27017/test?ssl=true&replicaSet=Cluster1-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.new_db



def add_student(name,age,roll,branch):
    unique_employee = db.students.find_one({"roll":roll})
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
        
        
add_student('Ashwani',19,5,'ML/AI')
add_student('Ankit',19,3,'ML/AI')
add_student('Lavish',18,6,'ML/AI')
add_student('Vishal',19,7,'ML/AI')
add_student('Lokesh',20,8,'ML/AI')


fetch_all_student()