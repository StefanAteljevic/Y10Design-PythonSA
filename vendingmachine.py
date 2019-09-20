
print("Hello and welcome to the Stefan vending machine!")

print("1. GoGo Juice ~ $7.99")

print("2. Funyons ~ $0.15 (per funyon)")

print("3. Carrot Cake ~ $39.99")

choice = int(input("What would you like to eat? Please pick a number from 1 to 3.\n"))

if choice == 1:
    print("You have purchased GoGo Juice! What a unique individual! (Amount paid ~ $7.99)")
elif choice == 2:
    print ("We only have one funyon in stock! Have fun! (Amount Paid ~ $0.15)")
elif choice == 3:
    print ("You have purchased Carrot Cake! Ew! (Amount Paid ~ $39.99)")
else:
    print ("This is not a valid choice...")
    print ("Please try again!")

input("Press ENTER to quit the program. Please only do this after you have paid as we   need money. Like, really badly.")