'''Iteration 3
Add the following features to your first iteration:

 Ask the user whether they would like french fries (yes, no).
 If they say yes, ask what size french fries they would like: 
    small $1.00
    medium $1.50
    large $2.00
 If they say “small,” ask the user whether they’d like to mega-size their fries (yes, no). 
 If the user inputs yes to mega-size, give them large fries at the large fries price instead of their small fries.
 Have the program output the user’s fries selection to verify that the program is working correctly.
 Adjust the program so the total cost only outputs to the user after their sandwich, drink, and fries selection.'''
def startUp():
    greeting = input("Welcome to Mason's Resturant! What would you like to order? \n Options: \n -Chicken 5.25 \n -Beef 6.75 \n -Tofu 5.75 \n > " )  
   
    price = 0
    if greeting == "Chicken" or greeting == "chicken" or greeting == "CHICKEN":
        price = 5.25
        print(greeting, "? ")
    elif greeting == "Beef" or greeting == "beef" or greeting == "BEEF":
        price = 6.75
        print(greeting, "? ")
    elif greeting == "Tofu" or greeting == "tofu" or greeting == "TOFU":
        price = 5.75
        print(greeting, "? ")
    else :
            price = 0
            print("Invaild answer! please check what you've typed!")
            return 0 

    askfordrink = input("Would you like a drink? > ")
    if askfordrink == "yes" :
           print( "Options: \n -Small 1.00 \n -Medium 1.75 \n -Large 2.25 \n > ")
           askfordrink = input("What size? > ")
    if askfordrink == "Small" or askfordrink == "small" or askfordrink == "SMALL":
        price = price + 1
        print(askfordrink, "? ")
    elif askfordrink == "Medium" or askfordrink == "medium" or askfordrink == "MEDIUM":
        price = price + 1.75
        print(askfordrink, "? ")
    elif askfordrink == "Large" or askfordrink == "large" or askfordrink == "LARGE":
        price = price + 2.25
        print(askfordrink, "? ")
    else :
            price = 0
            print("Invaild answer! please check what you've typed!")
            return 0 
   
    askforfries = input("Would you like fries with your meal? > ")
    if askforfries == "yes" :
           print( "Options: \n -Small 1.00 \n -Medium 1.75 \n -Large 2.25 \n > ")
           askforfries = input("What size? > ")
    if askforfries == "Small" or askforfries == "small" or askforfries == "SMALL":
        price = price + 1
        askforfries = input("Would you like to supersize? \n > ")
        if askforfries == "yes":
             price = price + -1 + 2
        print(askforfries, "? " , "\n subtotal: $" , str((price)) + "0")
    elif askforfries == "Medium" or askforfries == "medium" or askforfries == "MEDIUM":
        price = price + 1.50
        print(askforfries, "? " , "\n subtotal: $" , str((price)) + "0")
    elif askforfries == "Large" or askforfries == "large" or askforfries == "LARGE":
        price = price + 2
        print(askforfries, "? " , "\n subtotal: $" , str((price)) + "0")
    else :
            price = 0
            print("Invaild answer! please check what you've typed!")
            return 0
startup()
