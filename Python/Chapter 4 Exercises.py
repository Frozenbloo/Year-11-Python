#Chapter 4 Exercises | Tom Bloomer

#Exercise 1
'''
import random

total = 0
for x in range (10):
    No = random.randint(1,10)
    print(No)
    total += No

print(total)

#Exercise 2

import random
total = 0
for y in range(1000):
  for x in range (10):
     No = random.randint(1,10)
     total += No

avg = total/1000
print(avg)

'''
#Exercise 3
     
AB = 0
AS = 0
Num00 = 0
Code = "a"

while Code != "Done":
  Code = input("Please Enter Your 5 Digit Product Codes. To Exit Type Done  : ")
  ABstart = Code[0:2]
  end00 = Code[3:5]
  if ABstart == "AB":
      AB = AB + 1
  if ABstart == "AS":
     AS = AS + 1
  if end00 == "00":
      Num00 = Num00 + 1

print("Codes Starting With AB =",AB,"\nCodes Starting With AS =",AS) 
print("Codes Ending In 00 =" ,Num00)


