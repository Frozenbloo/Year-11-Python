#Tom Bloomer - Python Assignment(Lists)

#Task Number 1

'''
choice = 0
shoppingList = []
item = ""

while choice != "3":
    print("\nShopping System:\nAdd Item:\t\tPress 1\nRemove Last Item:\tPress 2\nQuit:\t\t\tPress 3\n")
    choice = input("Please Choose an Option: ")
    if choice == "1":
        while item != "Back":
            print("\n")
            item = input("Please Enter The Item You Would Like To Add, Enter Back To Enter The Menu: ")
            shoppingList.append(item)
            if "Back" in shoppingList:
                shoppingList.pop()
                print("\nYour Shopping List;")
                print(shoppingList)
            else:
                print("\nYour Shopping List;")
                print(shoppingList)
            
    if choice == "2":
        shoppingList.pop()
        print("\nYour Shopping List;")
        print(shoppingList)
    if choice > "3":
        print("\nSorry, That Isn't A Valid Option")

print("\nYour Final Shopping List Was;")
print(shoppingList)
'''

#Task Number 2

'''
studentNames = [["Doc"],["Sarah"],["Jar-Jar"],["Jake"],["Ben"],["BB8"],["R2D2"],["Gollum"],["Frodo"],["Snoke"]]
score = 0
length = len(studentNames)
y = 0

for x in range(10):
    name = studentNames[y+x][0]
    print("Enter The Test Score For",name)
    score = input("Test Score: ")
    studentNames[y+x].insert(0,score)

print("\nSTUDENT MARKS")
for o in range(10):
    print(studentNames[o])


sortedStudentNames = sorted(studentNames, reverse = True)

print("\nSORTED STUDENT MARKS")
for p in range(10):
    print(sortedStudentNames[p])
'''

#Task Number 3

'''
fornameList = ["Doc", "Sarah", "Jar-Jar", "Jake", "Ben"]
surnameList = ["Walker", "Conor", "Binks", "Drennan", "Solo"]
houseList = ["Armour", "Ross", "Calvert", "Calvert", "Ross"]
formClass = ["12W", "8M", "11T", "9S", "10R"]

joinedList = [fornameList, surnameList, houseList, formClass]

for x in range(4):
    print(joinedList[x])

print("\nThe Value at Row 1 and Column 2 is:",joinedList[1][2],"\nThe Value at Row 3 and Column 0 is:",joinedList[3][0],\
      "\nThe Value at Row 0 and Column 0 is:",joinedList[0][0],"\nThe Value at Row 0 and Column 4 is:",joinedList[0][4],"\nThe Value at Row 3 and Column 3 is:",joinedList[3][3])
'''

#Extra Part To Task Number 3(I repasted all the lists so it can be used when task 3 is commented out)

'''
fornameList = ["Doc", "Sarah", "Jar-Jar", "Jake", "Ben"]
surnameList = ["Walker", "Conor", "Binks", "Drennan", "Solo"]
houseList = ["Armour", "Ross", "Calvert", "Calvert", "Ross"]
formClass = ["12W", "8M", "11T", "9S", "10R"]

joinedList = [fornameList, surnameList, houseList, formClass]
row = 0
column = 0

for x in range (4):
    print(joinedList[x])

while row != "9" or column != "9":
    row = int(input("\nPlease Enter The Row Number You'd Like To Select, Enter 9 To Finish: "))
    column = int(input("\nPlease Enter The Column Number You'd Like To Select, Enter 9 To Finish: "))
    if row or column == "9":
        break
    print("\nThe Value at Row",row,"and Column",column,"is:",joinedList[row][column])
'''

#Task Number 4

'''
OlympicVenues = [["1980","Moscow","U.S.S.R."],["1984","Los Angeles","United States"],["1988","Seoul","South Korea"],["1992","Barcelona","Spain"],["1996","Atlanta","United States"]\
                 ,["2000","Sydney","Australia"],["2004","Athens","Greece"],["2008","Beijing","China"],["2012","London","United Kingdom"],["2016","Rio de Janeiro","Brazil"],["2020","Tokyo","Japan"]]

venue = 0
length = len(OlympicVenues)

while venue != "End":
    OlympicVenue = False
    venue = input("\nPlease enter a venue city or country: ")
    for n in range (length):
        if venue == "End":
            break
        if venue in OlympicVenues[n]:
            OlympicVenue = True
    if not OlympicVenue:
        print("\nNo",venue,"is NOT an Olympic venue!")
    else:
        print("\nYes",venue,"is an Olympic Venue!")
'''

#Task Number 5

'''
studentName = ["Doc","Sarah","Jar-Jar","Jake","Ben"]
incorrectMark = [72,75,23,54,48]
adjustmentFactor = [1.25,1.1,1.8,1.3,0.9]
adjustedMarks = []
Table = [studentName,incorrectMark,adjustmentFactor,adjustedMarks]
adjustedMark = 0

for x in range (5):
    adjustedMark = incorrectMark[x] * adjustmentFactor[x]
    adjustedMarks.append(adjustedMark)


print("\n")

for y in range (4):
    print(Table[y])
'''

    









    

