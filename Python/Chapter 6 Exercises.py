#Chapter 6 | Exercises | Tom Bloomer

#Exercise One

'''
average = 0
check = 0

while check == 0:
    tickets1 = int(input("Please Enter The Tickets Sold For Performance One: "))
    if tickets1 > 0 and tickets1 <= 120:
        average = average + tickets1
        check = 1
    else:
        print("Sorry, that is an invalid Number, Please Try Again")

while check == 1:
    tickets2 = int(input("\nPlease Enter The Tickets Sold For Performance Two: "))
    if tickets2 > 0 and tickets2 <= 120:
        average = average + tickets2
        check = 2
    else:
        print("Sorry, that is an invalid Number, Please Try Again")

while check == 2:
    tickets3 = int(input("\nPlease Enter The Tickets Sold For Performance Three: "))
    if tickets3 >0 and tickets3 <= 120:
        average = average + tickets3
        check = 3
    else:
        print("Sorry, that is an invalid Number, Please Try Again")

while check == 3:
    tickets4 = int(input("\nPlease Enter The Tickets Sold For Performance Four : "))
    if tickets4 > 0 and tickets4 <= 120:
        average = average + tickets4
        check = 4
    else:
        print("Sorry, that is an invalid Number, Please Try Again")



if check == 4:
    print("\nThe Total Number Of Tickets Sold Was",average)
    average = average / 4
    print("\nThe Average Number Of Attendees Was",average)

'''

#Exercise Two

'''
import re
carReg = 0

while carReg != "End":
    carReg = input("Please Enter Your Car Registration Number, Enter End To Quit: ")
    validCarReg = re.match("[A-Z]{2,}[0-9]{2,}[ | ]{1,}[A-Z]{3,}", carReg)
    if validCarReg:
        print("Car Registration Accepted")
    elif carReg == "End":
        break
    else:
        print("Invalid Car Registration Entered, Please Try Again")
'''


#Exercise Three

'''
email = 0
check = 0

while check == 0:
    email = input("\nPlease Enter Your Email Address: ")
    if "@" in email and "." in email:
        print("\nEmail Accepted")
        check = 1
    else:
        print("\nThat Is Not A Valid Email, Please Try Again")
    while check == 1:
        email2 = input("\nPlease Enter Your Email Address For A Second Time: ")
        if email == email2:
            print("\nEmail Address Is Verified and Accepted")
        else:
            print("\nSorry Email Is Invalid")
            check = 0

'''

#Exercise Four

'''
verified = 0

while verified != 4:
    Password = input("Please Enter A New Password: ")
    for index in range(len(Password)):
        if len(Password) >= 8 and len(Password) <= 15:
            if ord(Password[index]) in range(65,91):
                if ord(Password[index]) in range(48,57):
                    if ord(Password[index]) in range(97,122):
                        verified = verified + 1
                    verified = verified + 1
                verified = verified + 1
            verified = verified + 1
    if verified >= 4:
        print("Password Accepted")
        break
    else:
        print("Sorry, thats an invalid password!\nTo Strengthen your password, Please Use At Least 1 Uppercase, Lowercase And Numerical Value, and Always Make Sure It Is Between 8 and 15 Characters Long!")
'''
