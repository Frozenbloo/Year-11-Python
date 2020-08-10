#Chapter 9 Exercises | Tom Bloomer

#Exercise 1

studentFile = open("students.txt", "w")

studentFile.write("tbloomer" + "," + "Tom" + "," + "Bloomer" + "," + "Male" + "," + "11" + "," + "\n")
studentFile.write("npatterson" + "," + "Noah" + "," + "Patterson" + "," + "Male" + "," + "11" + "," + "\n")
studentFile.write("dprice" + "," + "Daniel" + "," + "Price" + "," + "Male" + "," + "11" + "," + "\n")
studentFile.write("leliot" + "," + "Lauren" + "," + "Eliot" + "," + "Female" + "," + "13" + "," + "\n")
studentFile.write("jmurray" + "," + "Jessica" + "," + "Murray" + "," + "Female" + "," + "10" + "," + "\n")
studentFile.write("sthompson" + "," + "Sarah" + "," + "Thompson" + "," + "Female" + "," + "10" + "," + "\n")
studentFile.write("ibloomer" + "," + "Isaac" + "," + "Bloomer" + "," + "Male" + "," + "9" + "," + "\n")

studentFile.close()


#Exercise 2

studentFile = open("students.txt", "r")
students = studentFile.readline()

print("%-13s%13s%13s"
      %("Username","FirstName","Surname"))

while students != "":
    field = students.split(",")
    Username = field[0]
    FirstName = field[1]
    Surname = field[2]
    Gender = field[3]
    Year = field[4]
    if Gender == "Female" and Year == "10":
        print("%-13s%13s%13s"
              %(Username,FirstName,Surname))
    students = studentFile.readline()
studentFile.close()


#Exercise 3

print("\n")

studentFile = open("students.txt", "r")


studentTable = []
StudentRec = []

for students in studentFile:
    field = students.split(",")
    Username = field[0]
    FirstName = field[1]
    Surname = field[2]
    Gender = field[3]
    Year = field[4]


    studentTable.append(Surname)
    studentTable.append(FirstName)
    studentTable.append(Gender)
    studentTable.append(Year)

    StudentRec.append(studentTable)

    studentTable = []


    sortedTable = sorted(StudentRec, key = lambda x:x[0])


print("%-20s%20s%20s%20s"
      %("Surname","Firstname","Gender","Year"))
for n in range(len(sortedTable)):
    print("%-20s%20s%20s%20s"
          %(sortedTable[n][0],sortedTable[n][1],sortedTable[n][2],sortedTable[n][3]))



    


    
