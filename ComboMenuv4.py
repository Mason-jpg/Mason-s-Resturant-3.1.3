'''Iteration 4
 Ask the user how many ketchup packets they would like (enter a positive integer; cost is $0.25 per packet).

After ordering the sandwich, drink, fries, and ketchup packets:
 If the user selected a sandwich, french fries, and a beverage, reduce the total cost of the order by $1.00.
 The program informs the user of their menu selections, for only the items they ordered. 
 The program should print the total cost of the order. Remove any other totals before this point.'''
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
        print(askforfries, "? " )
    elif askforfries == "Medium" or askforfries == "medium" or askforfries == "MEDIUM":
        price = price + 1.50
        print(askforfries, "? ")
    elif askforfries == "Large" or askforfries == "large" or askforfries == "LARGE":
        price = price + 2
        print(askforfries, "? ")
    if askforfries == "no":
         print()
    else :
            price = 0
            print("Invaild answer! please check what you've typed!")
            return 0 
  
    askfork = input("Would you like ketchup? > ")
    if askfork == "yes" :
           askfork = input("How many packets? (maximum 5 per customer) > ")
    if askfork == "1":
        price = price + 0.25
        print(askfork, "? " , "\n subtotal: $" , str((price)) + "0")
    elif askfork == "2":
        price = price + 0.50
        print(askfork, "? " , "\n subtotal: $" , str((price)) + "0")
    elif askfork == "3":
        price = price + 0.75
        print(askfork, "? " , "\n subtotal: $" , str((price)))
    elif askfork == "4":
        price = price + 1
        print(askfork, "? " , "\n subtotal: $" , str((price)) + "0")
    elif askfork == "5":
        price = price + 1.25
        print(askfork, "? " , "\n subtotal: $" , str((price)))
    if price == 10.25:
        price = price - 1
    else :
            price = 0
            print("Thank you! Come again!")
            return 0 
startUp()

