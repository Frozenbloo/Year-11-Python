choice = 0
studentFile = open("AQE Students.txt","r")
studentslist = []
newStudentsList = []
adjFactor = ""
passMark = int(0)

CandidateNoList = []
FirstNameList = []
LastnameList = []
AQEScore1List = []
AQEScore2List = []
AQEScore3List = []


adj1 = [1.2,1.4,1.1]
adj2 = [1.3,1.1,1.2]
adj3 = [1.1,1.4,1.3]


for row in studentFile:
    studentRec = row.split(",")
    CandidateNo = studentRec[0]
    FirstName = studentRec[1]
    Lastname = studentRec[2]
    AQEScore1 = int(studentRec[3])
    AQEScore2 = int(studentRec[4])
    AQEScore3 = int(studentRec[5])

    newStudentsList.append(CandidateNo)
    newStudentsList.append(FirstName)
    newStudentsList.append(Lastname)
    newStudentsList.append(AQEScore1)
    newStudentsList.append(AQEScore2)
    newStudentsList.append(AQEScore3)

    CandidateNoList.append(CandidateNo)
    FirstNameList.append(FirstName)
    LastnameList.append(Lastname)
    AQEScore1List.append(AQEScore1)
    AQEScore2List.append(AQEScore2)
    AQEScore3List.append(AQEScore3)

    studentslist.append(newStudentsList)
    newStudentsList = []

"""
print(CandidateNoList)
print(FirstNameList)
print(LastnameList)
print(AQEScore1List)
print(AQEScore2List)
print(AQEScore3List)
print("\n")
print(studentslist)
""" 


studentFile.close()


def enterAdjustmentFactor():
    global adjFactor
    adjFactor = input("Please enter the 4 Digit Code for the Adjustment Factor to use: ")
    if adjFactor != "adj1" and adjFactor != "adj2" and adjFactor != "adj3":
        print("Sorry - your entry must be adj1, adj2 or adj3")
        adjFactor = ""
        menu()
    else:
        print("Adjustment Factor Accepted - your chosen Adjustment Factor is ", adjFactor)
    menu()

def exit():
    print("Program Terminated")
    quit()

def applyAdjFactor():
    adjustedScoresList = []
    adjustedScoresRow = []

    if adjFactor == "":
        print("There is no Adjustment Factor Entered so no Adjustments can be made!")
        menu()
    else:
        print("The adjustment Factor : ",adjFactor, "will be used in this analysis")

    if adjFactor == "adj1":
        for x in range (12):
            adjustedScoresRow.append(studentslist[x][0])
            adjustedScoresRow.append(studentslist[x][1])
            adjustedScoresRow.append(studentslist[x][2])
            newAdjGrade1 = round(float(studentslist[x][3]*adj1[0]),2)
            newAdjGrade2 = round(float(studentslist[x][4]*adj1[1]),2)
            newAdjGrade3 = round(float(studentslist[x][5]*adj1[2]),2)
            adjustedScoresRow.append(newAdjGrade1)
            adjustedScoresRow.append(newAdjGrade2)
            adjustedScoresRow.append(newAdjGrade3)
            adjustedScoresList.append(adjustedScoresRow)
            adjustedScoresRow = []
    elif adjFactor == "adj2":
        for x in range (12):
            adjustedScoresRow.append(studentslist[x][0])
            adjustedScoresRow.append(studentslist[x][1])
            adjustedScoresRow.append(studentslist[x][2])
            newAdjGrade1 = round(float(studentslist[x][3]*adj2[0]),2)
            newAdjGrade2 = round(float(studentslist[x][4]*adj2[1]),2)
            newAdjGrade3 = round(float(studentslist[x][5]*adj2[2]),2)
            adjustedScoresRow.append(newAdjGrade1)
            adjustedScoresRow.append(newAdjGrade2)
            adjustedScoresRow.append(newAdjGrade3)
            adjustedScoresList.append(adjustedScoresRow)
            adjustedScoresRow = []
    elif adjFactor == "adj3":
        for x in range (12):
             adjustedScoresRow.append(studentslist[x][0])
             adjustedScoresRow.append(studentslist[x][1])
             adjustedScoresRow.append(studentslist[x][2])
             newAdjGrade1 = round(float(studentslist[x][3]*adj3[0]),2)
             newAdjGrade2 = round(float(studentslist[x][4]*adj3[1]),2)
             newAdjGrade3 = round(float(studentslist[x][5]*adj3[2]),2)
             adjustedScoresRow.append(newAdjGrade1)
             adjustedScoresRow.append(newAdjGrade2)
             adjustedScoresRow.append(newAdjGrade3)
             adjustedScoresList.append(adjustedScoresRow)
             adjustedScoresRow = []

    print(adjustedScoresList)

    individualAnalysis = input("Please enter the Candidate Number for the student you wish to analyse: ")
    adjustedStudentScoresListLength = len(adjustedScoresList)

    foundStudent = False

    for i in range (adjustedStudentScoresListLength):
        if individualAnalysis in adjustedScoresList[i][0]:
            print("Candidate Number at Position ",i)
            foundStudent = True
            studentIndex = i
            print("This is the analysis of the following student: ")
            print("Forename: ",adjustedScoresList[i][1])
            print("Surname: ",adjustedScoresList[i][2])
            print("Adjusted Score 1: ",adjustedScoresList[i][3])
            print("Adjusted Score 2: ",adjustedScoresList[i][4])
            print("Adjusted Score 3: ",adjustedScoresList[i][5])
            averageScore = round((adjustedScoresList[i][3] + adjustedScoresList[i][4] + adjustedScoresList[i][5])/3,2)
            print("Average Score: ",averageScore)
    if not foundStudent:
        print("The Candidate number that you entered must not be correctly entered. Please Try Again.")
        menu()
            
    applyPassMark = input("Do you wish to apply the School's passmark to the individual analysis anove? (Y or N)")
    if applyPassMark == "Y":
        if passMark == 0:
            print("Sorry - No Pass Mark has been set yet! Select Option 7 to set one!")
            menu()
        else:
            print("The passmark is currently set to ",passMark)
            print(":::::STUDENT ENTRY _ NON ENTRY SUMMARY:::::")
            print("Forename: ",adjustedScoresList[studentIndex][1])
            print("Surname: ",adjustedScoresList[studentIndex][2])
            print("Average Score: ",averageScore)
            if averageScore >= passMark:
                print("CONGRATULATIONS - you have gained a place at your chosen school")
            else:
                print("SORRY - your score of ",averageScore," dose not exceed the Pass Mark for your school of ",passMark)
    elif applyPassMark == "N":
        menu()

def setPassMark():
    global passMark
    passMark = int(input("Please enter the Pass Mark to gain entry to the school: "))
    print("The PASS MARK currently set for the school is ",passMark)
            


    

def menu():
    choice = ""
    while choice != "0":
        print("\n")
        print(" ~~ A Q E     R E S U L T S ~~")
        print("\n")
        print("Press 1 to print a 1D List of Forenames")
        print("\n")
        print("Press 2 to print a 1D List of Surnames")
        print("\n")
        print("Press 3 to print a 2D List")
        print("\n")
        print("Press 4 to QUIT")
        print("\n")
        print("Press 5 to set the Adjustment Factor")
        print("\n")
        print("Press 6 to apply the Adjustment Factor")
        print("\n")
        print("Press 7 to set the Pass Mark for the school")
        print("\n")
        choice = str(input("Please type the number that is beside your choice and press enter: "))
        if choice == "1":
            print(FirstNameList)
        elif choice == "2":
            print(LastnameList)
        elif choice == "3":
            print(studentslist)
        elif choice == "4":
            exit()
        elif choice == "5":
            enterAdjustmentFactor()
        elif choice == "6":
            applyAdjFactor()
        elif choice == "7":
            setPassMark()
        else:
            print("Choice is invalid, please try again")

menu()
                     

    
