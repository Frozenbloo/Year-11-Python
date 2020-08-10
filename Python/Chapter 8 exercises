#Tom Bloomer | Chapter 8 Examples

#Example 1

def getAndPrintName():
    name = input("Please enter your name: ")
    print("Hello",name)

getAndPrintName()


#Example 2
def getAndPrintName(message):
    name = input("Please enter your name: ")
    print(message, name)
    return name

playerName = getAndPrintName("Hello")
print(playerName, "is Player 1")


#Example 3

def DisplayRules():
    print("""
    The Rules of the game are as follows:
    Players take turns to throw two dice.
    If the throw is a 'double', ect.
        """)

DisplayRules()


#Example 4

def findAverage(x,y,z):
    total = x + y + z
    average = total/3
    return average


print("""This Program uses a function
to find the average of 3 numbers \n""")
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))
result = findAverage(num1, num2, num3)
print("Average is ",result)


#Example 5

print("\n")
def findAverage(x,y,z):
    total = x + y + z
    average = total/3
    return average


def printHeading():
    print("This Program uses a function",
    "to find the average of 3 numbers \n")

def UserInput():
    n1 = float(input("Enter First Number: "))
    n2 = float(input("Enter Second Number: "))
    n3 = float(input("Enter Third Number: "))
    return n1, n2, n3

def printResult(answer):
    print("Average is ",answer)


printHeading()
num1, num2, num3 = UserInput()
average = findAverage(num1, num2, num3)
printResult(average)


#Example 6

print("\n")
def nameOne():
    myName = "Alice"
    print("In function nameOne, name = ", myName)

def nameTwo():
    myName = "Bob"
    print("In function nameTwo, name = ", myName)

myName = "Kumar"
print("In main program, name = ", myName)
nameOne()
print("In main Program, name = ", myName)
nameTwo()
print("In main Program, name = ", myName)


#Example 7

print("\n")
def nameOne():
    global myName
    print("In Function nameOne, name = ", myName)
    myName = "Alice"
    print("In Function nameOne, name = ", myName)

def nameTwo():
    myName = "Bob"
    print("In Function nameTwo, name = ", myName)

myName = "Kumar"
print("In main program, name = ", myName)
nameOne()
print("In main program, name = ", myName)
nameTwo()
print("In main program, name = ", myName)


