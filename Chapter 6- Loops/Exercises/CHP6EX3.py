#Using while loop for the infinity loop
while True:
    #Asking user their age
    age = input("How old are you? ")
    age = int(age) #Gathers user input information
    #Using if function for the output
    if age < 17: #If user is under 17, outputs the message below
        print("You can't get your drivers licence yet! :<\n")
    else:  #Else outputs the message below
        print("Your can get your driver licence! :3\n")