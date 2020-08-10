astring = "You've done a good job!"
print("Original string:",astring)
print("Uppercase String:",astring.upper())
print("New String:",astring.replace("good","brilliant"))
print("Original String:",astring)
print("The Word done starts at index",astring.index("done"))

main = float(input("Enter cost of main course: "))
juice = float(input("Enter cost of juice: "))
banana = float(input("Enter cost of banana: "))
total = main + juice + banana
print("%-16s%5.2f" %("Total for lunch: ",total))

numchars = len(astring)
print(astring)
