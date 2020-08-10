#Tom Bloomer | Chapter 3
"""
#Exercise 1
length = float(input("Please Input The Length: "))
width = float(input("Please Input The Width: "))
area = (length * width)
roundedArea = round(area , 2)
if length == width:
            print("This Is A Square With An Area Of",roundedArea)
else:
            print("This Is A Rectangle With An Area Of",roundedArea)
"""

#Exercise 2
"""
print("Menu")
print("1. Music")
print("2. History")
print("3. Design and Technology")
print("4. Exit")
choice = int(input("Please Enter Your Choice: "))
if choice == 1:
    print("You Chose Music")
elif choice == 2:
    print("You Chose History")
elif choice == 3:
    print("You Chose Design and Technology")
elif choice == 4:
    print("Goodbye")
else:
    print("That Is Not A Valid Input.")
"""

#Exercise 3
"""
import random
throw1 = random.randint(1,6)
throw2 = random.randint(1,6)
if throw1 == throw2:
    print("You Threw A Double! You Threw:",throw1 * throw2)
else:
    print("You Threw:",throw1 * throw2)
"""

#Exercise 4

value = int(input("Please Enter The Value Of The Goods: "))
if value > 200:
    print("The Value Of The Goods Was",value,",but because you spend over £200, you get a 10% Discount! \n The New Value Of The Goods Is:",value * 0.9)
elif value > 100:
    print("The Value Of The Goods Was",value,",but because you spend between £100 and £199.99, you get a 5% Discount! \n The New Value Of The Goods Is:",value * 0.95)
else:
    print("The Value Of The Goods Is", value)
