#Vending Machine
#Stefan Ateljevic
#UCC


print("Hello and welcome to the Stefan vending machine!")
print("")
print("1. Apple Juice")
print("2. Funyuns")
print("3. Carrot Cake")

#money = int(input("How much money would you like to input?"))
print("")
choice = int(input("What would you like to purchase? Please pick a number from 1 to 3.\n"))

money = 0

if choice == 1:
    money = float(input("Please input money. One can is $4.00. \n" ))
    appleans = int(input("\nHow many cans would you like?"))
    appletotal = int(4*int(appleans))
    print("\nThe total price is $" + str(appletotal))
if money == 4.0:
	print("\nHere is your apple juice. Have a great day!")
elif money < 4.0:
	print("\nInsufficient funds. Please try again.")
elif money > 4.0:
	print("\nHere are your apple juices. Have a great day!")

money2 = 0

if choice == 2:
	money2 = float(input("Please input money. One funyun is $0.15. \n"))
	funyunans = int(input("\nHow many funyuns would you like?")) 
	funyuntotal = int(0.15*int(funyunans))
	print("\nThe total price is $" + str(funyuntotal))
if money2 == 0.15:
	print("\nHere is your funyun. Have a great day!")
elif money2 < 0.15:
	print("\nInsufficient funds. Please try again.")
elif money2 > 0.15: 
	print("\nHere are your funyuns. Have a great day!")


elif choice == 3:
    print ("The price for Carrot Cake is $9.99")
    carrotans = int(input("How many pieces of Carrot Cake would you like?"))
    carrottotal = int(9.99*int(carrotans))
    print("The total price is $" + str(carrottotal))
else:
    print ("This is not a valid choice...")
    print ("Please try again!")

print("")

print ("Thank you for shopping at the Stefan vending machine. See you soon!")

print("")

input("Press ENTER to quit the program.")