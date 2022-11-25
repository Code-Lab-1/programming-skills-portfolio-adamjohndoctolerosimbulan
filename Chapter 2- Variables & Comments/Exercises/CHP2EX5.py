#Assigning the variables
#Asking user to enter the money
cash = int(input("\nUSB sticks costs £6, insert your amount of cash: "))
value = int(6)
answer = cash//value
confirm = int(1)
#If user buys 8 sticks it outputs the first if statement
if answer == (8) :
    cash = int(input("\n8 USB sticks cost £48.\nWould you like to buy it?\n1 Yes \n2 No\n"))
    if cash == confirm: 
        print("\nYou bought 8 USB sticks\nChange: £2\n")
    #else outputs this message
    else: 
        print("\nTransaction Cancelled")