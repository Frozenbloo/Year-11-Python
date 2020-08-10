#Tom Bloomer - Python Test

#Task Number 1
'''
print("Please Input 5 Float Point Numbers To 3 Decimal Places;")
Num1 = float(input("Please Enter Your First Number: "))
Num2 = float(input("Please Enter Your Second Number: "))
Num3 = float(input("Please Enter Your Third Number: "))
Num4 = float(input("Please Enter Your Fourth Number: "))
Num5 = float(input("Please Enter Your Fifth Number: "))
NumSum = float(Num1 * Num2 * Num3 * Num4 * Num5)
NumAvg = float((Num1 + Num2 + Num3 + Num4 + Num5) / 5)
RoundNumSum = round(NumSum,3)
RoundNumAvg = round(NumAvg,2)
print("The Sum Of Your Five Floating Point Numbers is",RoundNumSum)
print("The Average Of Your Five Floating Point Numbers is",RoundNumAvg)
'''
#Task Number 2
'''
FavSportsTeam = input("Please Input Your Favorite Sports Team: ")
FormClass = input("Please Enter Your Form Class: ")
BirthMonth = input("Please Enter Your Birth Month: ")
print("My Favourite Sports Team is",FavSportsTeam,"and my current form class is",FormClass," My Month Of Birth Is",BirthMonth)
print("My Favourite Sports team is:\n" + FavSportsTeam)
print("\n")
print("My Current Form Class Is:\n" + FormClass)
print("\n")
print("My Month Of Birth Is:\n" + BirthMonth)
print("\n")
print("My Favourite Sports Team \t Current Form Class \t Month Of Birth\n" + FavSportsTeam + "\t\t\t\t",FormClass,"\t\t\t",BirthMonth)
'''
#Task Number 3
'''
Mins = int(input("Please Enter How Many Minutes Were Spent On The Internet: "))
Charge = float(0)
if Mins < 10:
    Charge = 1.00
elif Mins < 20:
      Charge = 2.00
elif Mins < 30:
        Charge = 2.75
elif Mins < 40:
          Charge = 3.50
elif Mins < 50:
            Charge = 4.00
elif Mins < 60:
                Charge = 5.50
elif Mins > 61:
                Charge = (Charge + 6.00)
roundedCharge = round(Charge,2)
print("You Have Used",Mins,"Minutes In DalCafe. Your Charge Will Be £",roundedCharge,". Thanks For Your Business.")
'''
#Task Number 4

Length = float(input("Please Enter The Length Of The Room: "))
Width = float(input("Please Enter The Width Of The Room: "))
Area = (Length * Width)
Permimiter = (Length + Width + Length + Width)
print("1. Calculate Permimeter")
print("2. Calculate Area")
print("3. Display The Longest Side")
print("4. Exit The System")
Choice = int(input("Please Enter Your Choice: "))
if Choice == 1:
    print("The Permimeter Of The Floorspace is:",Permimiter,"mSq.")
elif Choice == 2:
    print("The Area Of The Floorspace is:",Area,"mSq.")
elif Choice == 3:
    if Length > Width:
        print("The Longest Side Of The Floorspace Is",Length,"mSq.")
    else:
        print("The Longest Side Of The Floorspace Is",Width,"mSq.")
elif Choice == 4:
    print("Thanks For Using CarpetRite - Goodbye.")
else:
    print("Sorry, But That Isn't A Valid Option.")
    

             

                    
                            


