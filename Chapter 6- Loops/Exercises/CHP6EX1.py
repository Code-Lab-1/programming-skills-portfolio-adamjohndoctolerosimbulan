#Asks user what toppings to add
msg = "\nWhat kind of toppings would you prefer on your pizza?"
#Asks user to enter 'quit' when they are done
msg += "\nType'quit' when you are done: "

#Using while loop function
while True:
    toppings = input(msg) #Gathers users input
    if toppings != 'quit':
        #Displays the topping that the user entered
        print(f"  {toppings} is added to your pizza.") 
    else:
        break