    #salary calculator
#Q. An employee gets paid(hours worked)*(base pay), for each hours upto 40 hours, for every hour over 40 hours, they get ovewrtime =(base pay)*1.5. calculate total salary.

#storing base pay of the employee
basePay=input("enter the base pay of the employee   >")

#storing normal working hours of an employee
totalHours=input(" enter the total number of hours worked upto 40hours  >")

# storing extra hours worked by an employee
extraHours=input("extra hours worked   >")

#noraml pay of an employee
salary= (float(basePay)*totalHours)

#pay for extra hours
salaryForOvertime= (float(basePay)*1.5*extraHours)

#pay after including  overtime
totalSalary=salaryForOvertime+salary

#result
print(totalSalary)
