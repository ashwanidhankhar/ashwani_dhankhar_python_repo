import os
import csv

os.chdir("C:\\Users\\ashwa\\Desktop\\assignment_Python")

with open("zoo.csv") as csv_file:
    read=csv.reader(csv_file,delimiter=',')
    for row in read:
        print row
