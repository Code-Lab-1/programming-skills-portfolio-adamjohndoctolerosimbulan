#Adding values to a variable
names = ["Matt", "Adam", "Mei"]

#Prints the values based on it's position and the message
print( names[0], "you have been welcomed to join dinner on October 1st\n")
print( names[1], "you have been welcomed to join dinner on October 1st\n")
print( names[2], "you have been welcomed to join dinner on October 1st\n")
print("Mei is not available on October 1st, We should invite Apple\n")
names.insert(3, "Apple") #Inserts a new value to the list
print( names[3], "you have been welcomed to join dinner on October 1st")