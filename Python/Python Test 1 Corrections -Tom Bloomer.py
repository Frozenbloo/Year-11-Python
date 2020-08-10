#Python Test Corrections | Tom Bloomer

#Task One
No1 = float(input("Please enter your first floating point Number: "))
No2 = float(input("Please enter your second floating point Number: "))
No3 = float(input("Please enter your third floating point Number: "))
No4 = float(input("Please enter your fourth floating point Number: "))
No5 = float(input("Please enter your fifth floating point Number: "))
NoTotal = No1+No2+No3+No4+No5
NoAvg = (No1+No2+No3+No4+No5)/5
RoundedNoTotal = round(NoTotal,2)
RoundedNoAvg = round(NoAvg,3)
print ("The Sum Of The Five Floating Point Numbers is: ", RoundedNoTotal)
print ("The Average Of The Five Floating Point Numbers is: ", RoundedNoAvg)

#Task Two
favSportsTeam = input("Please Enter Your Favourite Sports Team: ")
FormClass = input("Please Enter Your Form Class: ")
MonthOfBirth = input("Please Enter Your Birth Month: ")
print ("My Favourite Sports Team Is "+favSportsTeam+", and my current form class is "+FormClass+". My Birth Month Is"+MonthOfBirth)
print ("My Favourite Sports Team Is: \n"+favSportsTeam+"\nMy current form class is: \n"+FormClass+"\nMy Birth Month Is: \n"+MonthOfBirth)
print ("My Favourite Sports Team\t\tMy current form class\t\tMy Birth Month")
print (favSportsTeam+"\t\t\t"+FormClass+"\t\t\t"+MonthOfBirth)

#Task Three
minsUsed = int(input("Please Enter The Number Of Minutes Connected To The Internet: "))
if minsUsed > 60:
    charge = " £6.00"
elif minsUsed >= 51:
    charge = " £5.50"
elif minsUsed >= 41:
    charge = " £4.00"
elif minsUsed >= 31:
    charge = " £3.50"
elif minsUsed >= 21:
    charge = " £2.75"
elif minsUsed >= 11:
    charge = " £2.00"
elif minsUsed <= 10:
    charge = " £1.00"

print ("You Have Used "+str(minsUsed)+" minutes In DalCafe. Your Charge Will Be" +charge)

#Task Four
length = float(input("Please Enter The Legnth Of The Room: "))
width = float(input("Please Enter The Width Of The Room: "))

print("Menu")
print("1. Calculate Perimeter")
print("2. Calculate Area")
print("3. Display Longest Side")
print("4. Exit The System")
choice = input("\nPlease Enter Your Choice: ")

if choice == "1":
    perimeter = (width*2)+(length*2)
    print("The Perimeter Of The Floorspace Is: "+str(perimeter)+" m")
elif choice == "2":
    Area = width*length
    print("The Area Of The Floorspace Is: "+str(Area)+" mSq")
elif choice == "3":
    if length>=width:
        longestSide = length
    else:
        longestSide = width
    print("The Longest Side Of The Floorspace Is: "+str(longestSide)+" m")
else:
    print("Thanks For Using CarpetRite - Goodbye")

input("\nPress Enter To Exit ")

#Task Five
print("1. Lord Of The Rings\n2. Star Wars")
choice = input("\nPlease Enter Your Choice: ")
if choice == "1":
    favFranchise = "Lord Of The Rings"
    print("1. The Fellowship of the Ring\n2. The Two Towers\n3. The Return Of The King")

    choiceLOTR = input("\nPlease Enter Your Favourite LOTR Movie: ")

    if choiceLOTR == "1":
        print("Thank You For Selecting Your Favourite "+favFranchise+" movie. Your Favourite Movie In That Franchise Is The Fellowship of The Ring")
    elif choiceLOTR == "2":
        print("Thank You For Selecting Your Favourite "+favFranchise+" movie. Your Favourite Movie In That Franchise Is The Two Towers")
    elif choiceLOTR == "3":
        print("Thank You For Selecting Your Favourite "+favFranchise+" movie. Your Favourite Movie In That Franchise Is The The Return Of The King")
elif choice == "2":
    favFranchise = "Star Wars"
    print("1. The Phantom Menace\n2. Attack Of The Clones\n3. Revenge Of The Sith\n4. Rogue One")

    choiceSW = input("\nPlease Enter Yuor Favourite SW Movie: ")

    if choiceSW == "1":
        print("Thank You For Selecting Your Favourite "+favFranchise+" movie. Your Favourite Movie In That Franchise Is The Phantom Menace")
    if choiceSW == "2":
        print("Thank You For Selecting Your Favourite "+favFranchise+" movie. Your Favourite Movie In That Franchise Is Attack Of The Clones")
    if choiceSW == "3":
        print("Thank You For Selecting Your Favourite "+favFranchise+" movie. Your Favourite Movie In That Franchise Is Revenge Of The Sith")
    if choiceSW == "4":
        print("Thank You For Selecting Your Favourite "+favFranchise+" movie. Your Favourite Movie In That Franchise Is Rogue One")

