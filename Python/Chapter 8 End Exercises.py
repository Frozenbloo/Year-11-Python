#Chapter 8 Exercises | Tom Bloomer

#Exercise 1


def SAreaAndVol():
    surfaceArea = (side * side) * 6
    Volume = side * side * side
    print("The Surface Area is",surfaceArea,"\nThe Volume is",Volume)

side = int(input("Please Enter The Side Length: "))
SAreaAndVol()


#Exercise 2

import random

def Encrypt():
    messageList = list(message)
    random.shuffle(messageList)
    print("".join(messageList))
    

message = input("Please Enter The Message you would like encrypted: ")
Encrypt()


#Exercise 3

TempList = []

def MaxTemp():
    Maxtemp = max(TempList)
    MaxDay = TempList.index(Maxtemp) + 1
    print("The Maximum Average Temperature was",Maxtemp,", which was on Day",MaxDay,".")

for x in range(7):
    daynumber = x + 1
    day = input("Please Enter The Average Daily Temperature for Day " + str(daynumber) + " : ")
    TempList.append(day)
MaxTemp()


#Exercise 4

def EmployeePay():
    weekPay = weekHours * payRate
    satPay = satHours * payRate * 1.5
    sunPay = sunHours * payRate * 2
    totalHours = weekHours + satHours + sunHours
    totalPay = weekPay + satPay + sunPay
    print("\n",Employee,"\n Total Hours Worked :",totalHours,"\n Total Pay :",totalPay)


Employee = input("Please Enter an Employee Name: ")
payRate = int(input("Please Enter Your Hourly Pay Rate: "))
weekHours = int(input("Please Enter The Hours Worked from Monday - Friday: "))
satHours = int(input("Please Enter the Hours Worked on Saturday: "))
sunHours = int(input("Please Enter The Hours Worked on Sunday: "))

EmployeePay()
