# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Put down some options for the user to choose from...

import datetime

print("1. Weather")
print("2. Date")
print("3. President of Yugoslavia from 1953 - 1980")
print(" ")

choice = int(input("What would you like to learn about? Please pick a number from 1 to 3.\n"))

if choice == 1:
    print("It is rainy and cloudy!")
elif choice == 2:
	now = datetime.datetime.now()

	print (now.strftime("%Y-%m-%d %I:%M"))
elif choice == 3:
    print ("TITO!")
else:
    print ("This is not a valid choice")
    print ("Hope you have a great day anyway!")


# This is a way to gracefuuly exit the program
input("Press ENTER to quit the program")
