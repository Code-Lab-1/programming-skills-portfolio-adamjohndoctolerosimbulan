#Listing all the sandwiches
sandwich_orders = ['BBQ Chicken', 'Grilled Cheese', 'Chicken Teriyaki', 'Smoked Turkey', 'Tuna', 'Pastrami']
finished_sandwiches = []

print("\n") #Adds a new line
#Displays that Pastrami isn't availabe
print("We're sorry, but we're out of Pastrami today.") 
while 'Pastrami' in sandwich_orders:
    #Removing the pastraming from the lsit
    sandwich_orders.remove('Pastrami') 
print("\n") #Adds a new line

#Using while loop to print preparing the sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm preparing your {current_sandwich} sandwich right away.")
    finished_sandwiches.append(current_sandwich)

print("\n") #Adds a new line
#Displays after the sandwhiches are prepared
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich is now prepared.")