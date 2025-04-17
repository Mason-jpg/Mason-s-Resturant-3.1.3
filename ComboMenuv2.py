'''Iteration 2
Add the following features to your first iteration:

 Ask the user whether they would like a beverage (yes, no).
 If they say yes, ask what size beverage they would like: 
    small $1.00
    medium $1.75
    large $2.25
 Have the program output the user’s beverage size selection, or lack of selection, to verify that the program is working correctly.
 Have the program output the total cost so far.'''
def startUp():
    greeting = input("Welcome to Mason's Resturant! What would you like to order? \n Options: \n -Chicken 5.25 \n -Beef 6.75 \n -Tofu 5.75 \n > " )  
   
    price = 0
    if greeting == "Chicken" or greeting == "chicken" or greeting == "CHICKEN":
        price = 5.25
        print(greeting, "? " , "\n subtotal: $" , price)
    elif greeting == "Beef" or greeting == "beef" or greeting == "BEEF":
        price = 6.75
        print(greeting, "? " , "\n subtotal: $" , price)
    elif greeting == "Tofu" or greeting == "tofu" or greeting == "TOFU":
        price = 5.75
        print(greeting, "? " , "\n subtotal: $" , price)
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
        print(askfordrink, "? " , "\n subtotal: $" , str((price)) + "0")
    elif askfordrink == "Medium" or askfordrink == "medium" or askfordrink == "MEDIUM":
        price = price + 1.75
        print(askfordrink, "? " , "\n subtotal: $" , str((price)) + "0")
    elif askfordrink == "Large" or askfordrink == "large" or askfordrink == "LARGE":
        price = price + 2.25
        print(askfordrink, "? " , "\n subtotal: $" , str((price)) + "0")
    else :
            price = 0
            print("Invaild answer! please check what you've typed!")
            return 0 
startUp()

