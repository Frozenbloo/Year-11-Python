# Tom Bloomer - Python Test 2

#Task Number 1
'''
for number in range (1,10):
    for length in range (0,number):
        print(number, end = "")
    print("\n")
'''

#Task Number 2

'''
import random
attempts = 0
Name = input("Please Enter Your Name: ")
No = random.randint(0,100)
for x in range(1,9):
    Guess = int(input("Please Enter a Number Between 1 & 100: "))
    attempts = x + 1
    if Guess == No:
        print("Congratulations" ,Name, "You Guessed The magic number of",No)
        break
    if Guess != No:
        if Guess < No:
            print("The magic number is more than your guess, you are too low")
        else:
            print("The magic number is less than your guess, you are too high")
    if attempts == 9:
        print("Hard luck", Name,"- You didn't manage to guess the magic number of",No)
        break
'''

#Task Number Three

'''
for x in range (5):
    print(x * " *")

for x in range (5,0,-1):
    print(x * " *")
'''

#Task Number Four

'''
TimesTable = int(input("Please Choose A Times Table To Be Quizzed On;\n\n1)One Times Tables\n2)Two Times Tables\n3)Three Times Tables\n4)Four Times Tables\n5)Five Times Tables\n6)Six Times Tables\n7)Seven \
Times Tables\n8)Eight Times Tables\n9)Nine Times Tables\n10)Ten Times Tables\n11)Eleven Times Tables\n12)Twelve Times Tables\n\nPlease Choose One To Start: "))

No1 = 1
ans = 0

print("\n")
print("The",TimesTable,"Times Tables")
print("\n")
for x in range (12):
    ans = No1 * TimesTable
    print(No1, "X", TimesTable, "=", ans)
    No1 = No1 + 1
'''


#Task Number Five

'''
AtIndex = False
Email = input("Please Enter Your Email Address: ")
for AtPos in range (len(Email)):
    if Email[AtPos] == "@":
        AtIndex = AtPos
        print("There is An @ Symbol In Your Email Address, At The Index Of",AtIndex)
        break

if AtIndex == False:
    print("There is No @ Symbol In Your Email Address")
'''

#Task Number Six

'''
VowelInd = -1
sentence = input("Please Enter A Sentence: ")
VowelNo = 0

for VowelPos in range(len(sentence)):
    if sentence[VowelPos] == "a":
        VowelInd = VowelPos
        VowelNo = VowelNo + 1
    if sentence[VowelPos] == "e":
        VowelInd = VowelPos
        VowelNo = VowelNo + 1
    if sentence[VowelPos] == "i":
        VowelInd = VowelPos
        VowelNo = VowelNo + 1
    if sentence[VowelPos] == "o":
        VowelInd = VowelPos
        VowelNo = VowelNo + 1
    if sentence[VowelPos] == "u":
        VowelInd = VowelPos
        VowelNo = VowelNo + 1


if VowelNo == 0:
    print("Sorry There Are No Vowels In This Sentence")

else:
    print("The Number of vowels in the entered sentence is:",VowelNo)
'''


#Task Number Seven

'''
VowelInd = -1
sentence = input("Please Enter A Sentence To Find Out Its Vowel Worth: ")
VowelPoints = 0

for VowelPos in range(len(sentence)):
    if sentence[VowelPos] == "a":
        VowelInd = VowelPos
        VowelPoints = VowelPoints + 5
    if sentence[VowelPos] == "e":
        VowelInd = VowelPos
        VowelPoints = VowelPoints + 4
    if sentence[VowelPos] == "i":
        VowelInd = VowelPos
        VowelPoints = VowelPoints + 3
    if sentence[VowelPos] == "o":
        VowelInd = VowelPos
        VowelPoints = VowelPoints + 2
    if sentence[VowelPos] == "u":
        VowelInd = VowelPos
        VowelPoints = VowelPoints + 1

print("The Vowel Worth of your word is:",VowelPoints)
'''
