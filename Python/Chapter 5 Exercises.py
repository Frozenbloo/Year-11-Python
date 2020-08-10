#Chapter Five Exercises | Tom Bloomer


#Exercise One
'''
alist = []
alist.append("apple")
blist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
clist = alist + blist
lastc = clist.pop()
'''

#Exercise Two
'''
nameinput = "a"
namelist = []
listno = 0

while nameinput != "End":
    nameinput = input("Please Enter A Name, Type 'End' to Finish : ")
    namelist.append(nameinput)
    listno = listno + 1

halflistno = listno // 2
halflist = namelist[0:halflistno]
print(halflist)
'''
#Exercise Three
'''
markList = []
avgMark = 0

name = input("Please Enter Your Name: ")

for x in range (10):
    marks = input("Please Enter Your Marks, One At A Time: ")
    markList.append(marks)
    avgMark = avgMark + int(marks)
    markList.sort(reverse = True)

sortedMarks = sorted(markList, reverse = True)
avgMark = (avgMark/10)
topmarks = markList[0:3]
bottommarks = markList[7:10]
print("\n" + name + " You recieved an average of :,",avgMark,"\nYour Top Three Marks Were: ",topmarks,"\nYour Worst Three Marks Were :",bottommarks)
'''

#Exercise Four
'''
monthName = ["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
monthlyAvg = []

for x in range(12):
    print("Please Enter The Average Maximum And Minumum Temperature For " + monthName[x])
    Maximum = int(input("Please Enter The Max Temperature :"))
    Minimum = int(input("Please Enter The Min Temperature :"))
    TableRow = [monthName[x], Maximum, Minimum]
    monthlyAvg.append(TableRow)

print("\n\n")

for m in range (12):
    for index in range(3):
        print(monthlyAvg[m][index],end = " ")
    print("\n")

highesttemp = -50
lowesttemp = 50
for m in range(12):
    month,Maximum,Minimum = monthlyAvg[m]
    if Maximum > highesttemp:
        highesttemp = Maximum
        hottestmonth = month
    if Minimum < lowesttemp:
        lowesttemp = Minimum
        coldestmonth = month
print("\nHottest Month", hottestmonth, ". Maximum temperature", highesttemp)
print("\nColdest Month", coldestmonth, ". Lowest temperature", lowesttemp, "\n")

'''
#Exercise Five

import random
UserID = "a"
GameList = [["UserID","TopScore"],["AAA01","135"],["BBB01","87"],["CCC01","188"],["DDD01","109"]]
playerscore = int(0)
oldplayerscore = 0
found = 0


    
while UserID != "xxx":
    UserID = input("Please Enter Your User ID :")
    u = GameList.index(UserID)
    if UserID not in GameList[u][0]:
        playerscore = random.randint(50,200)
        GameList.append([UserID, playerscore])
    if UserID in GameList[u][0]:
        print("yeet")
        
        


#Example 3

'''
studentNames = ["Khan, Afridi   ", "Milner, Angela   ",\
                "Philips, Justine", "Osmani, Pias   "]
results = []
topMark = 0
numberOfStudents = len(studentNames)

for student in range(numberOfStudents):
    print("Enter mark for",studentNames[student],": ",end = " ")
    mark = int(input())
    results.append(mark)
    if mark > topMark:
        topMark = mark
        topStudent = studentNames[student]

print("\nStudent\t\t\tExam mark")
for student in range(numberOfStudents):
    print(studentNames[student],"\t",results[student])

print("\nTop Result: ",topStudent,topMark)
'''
