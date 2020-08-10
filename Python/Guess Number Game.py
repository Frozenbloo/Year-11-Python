#Magic Number

import random
attempts = 0
Name = input("Please Enter Your Name: ")
No = random.randint(0,10)# << Check What The Random Number Is Between And Change
for x in range(1,9):
    Guess = int(input("Please Enter a Number Between 1 & 10: "))
    attempts = x + 1
    if Guess == No:
        print("Congratulations" ,Name, "You Guessed The Number In", x ,"Attempts!")
        break
    elif attempts == 9:
        print("Sorry", Name, "But You Couldn't Guess The Number In 8 Attempts! The magic number was",No)
        break

   
    
#Primary School Times Tables

TimesTable = int(input("Please Choose A Times Table To Be Quizzed On;\n1)One Times Tables\n2)Two Times Tables\n3)Three Times Tables\n4)Four Times Tables\n5)Five Times Tables\n6)Six Times Tables\n7)Seven Times Tables\n8)Eight Times Tables\n9)Nine Times Tables\n10)Ten Times Tables\n11)Eleven Times Tables\n12)Twelve Times Tables\nPlease Choose One To Start: "))

No1 = 1
ans = 0


for x in range (12):
    ans = No1 * TimesTable
    print("\n",No1,"x",TimesTable,"=",ans)
    No1 = No1 + 1
