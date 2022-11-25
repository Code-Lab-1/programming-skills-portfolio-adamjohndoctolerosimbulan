#Adding values to a variable
pangalan = ["Matt", "May", "Adam"]

#Prints the values based on it's position and the message
print(pangalan[0], "You have been welcomed to join dinner on October 1st.\n")
print(pangalan[1], "You have been welcomed to join dinner on October 1st.\n")
print(pangalan[2], "You have been welcomed to join dinner on October 1st.\n")

#Removes the value frome the list
pangalan.pop(2)
print("Adam is not available on October 1st, We should invite Ralph.")

#Adds a new value to the list
pangalan.insert(1,"Ralph")
print(pangalan[1], "You have been welcomed to join dinner on October 1st.\n")
print("Only two seats are available on the table!")
print(pangalan[0], "There is no seat left, sorry for the inconvenience.\n")

#Removes the value the list
People = pangalan.pop(0)

#Prints the new values and the message
print(pangalan[0], "due to the inconvenience you're still invited to join dinner on October 1st.\n")
print(pangalan[1], "due to the inconvenience you're still invited to join dinner on October 1st.\n")

#Deletes the values fromt he list
del(pangalan[0])
del(pangalan[0])