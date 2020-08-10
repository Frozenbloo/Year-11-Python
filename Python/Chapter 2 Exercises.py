#Tom Bloomer | Chapter 2

#Exercise 1

proverb = "A picture's worth a thousand words"
proverbImage = proverb.replace("A picture's","An image is")
firstO = proverb.index("o")
proverbUpper = proverb.upper()
proverbLength = proverb.find("")
print("Original String: ",proverb)
print("New String: ",proverbImage)
print("The Letter O starts at index: ",firstO)
print("Uppercase String: ",proverbUpper)
print("String Length: ",len(proverb))

#Exercise 2

print("\n")
radius = float(input("Please Enter The Radius Of The Circle: "))
Pi = float(3.14159)
Diameter = float(radius * 2)
two = float(2)
Area = Pi * radius ** two
Circumference = Pi * Diameter
AreaRound = round(Area,2)
CircumferenceRound = round(Circumference,2)
print("Area: ",Area)
print("Circumference: ",Circumference)
print("The Area To 2 Decimal Places Is: ",AreaRound)
print("The Circumference To 2 Decimal Places Is: ",CircumferenceRound)

#Exercise 3
print("\n")
num1 = float(input("Please Enter Your First Number: "))
num2 = float(input("Please Enter Your Second Number: "))
sum = num1 + num2
product = num1 * num2
sumround = round(sum,2)
productround = round(product,3)
print("The Sum Of Num1 and Num2 is ",sumround)
print("The Product of Num1 and Num2 is",productround)


