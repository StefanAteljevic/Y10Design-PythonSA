#Vending Machine
#Stefan Ateljevic
#UCC

print("Hello and welcome to the Stefan vending machine!")
print("")
print("1. GoGo Juice")
print("2. Funyons")
print("3. Carrot Cake")

#money = int(input("How much money would you like to input?"))
print("")
choice = int(input("What would you like to eat? Please pick a number from 1 to 3.\n"))

if choice == 1:
    print("The price for GoGo Juice is $4.00")
    gogoans = int(input("How many cans would you like?"))
    gogototal = int(4*int(gogoans))
    print("The total price is $" + str(gogototal))

elif choice == 2:
    print ("The price for a Funyon is $0.15")
    funyonans = int(input("How many funyons would you like?"))
    funyontotal = int(0.15*int(funyonans))
    print("The total price is $" + str(funyontotal))

elif choice == 3:
    print ("The price for Carrot Cake is $9.99")
    carrotand = int(input("How many pieces of Carrot Cake would you like?"))
    carrottotal = int(9.99*int(carrotans))
    print("The total price is $" + str(carrottotal))
else:
    print ("This is not a valid choice...")
    print ("Please try again!")

print ("Thank you for shopping at the Stefan vending machine. See you soon!")

input("Press ENTER to quit the program.")