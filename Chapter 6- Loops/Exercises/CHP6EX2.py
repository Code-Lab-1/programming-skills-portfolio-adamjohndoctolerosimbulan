#Displays & asks user their age 
msg = "\nHow old are you?"
msg += "\nEnter 'quit' when you are finished: " 

while True:
    age = input(msg) #Gathers user inputs
    if age == 'quit': #When the user enters 'quit' the program ends
        break
    age = int(age)

    #If the age is under 3 displays the message below
    if age < 3:
        print("  Your ticket is FREE!")
    #If the age is under 13 displays the message below    
    elif age < 13:
        print("  Your ticket is $10.")
    #If the age is over 13 displays the message below
    else:
        print("  Your ticket is $15.")