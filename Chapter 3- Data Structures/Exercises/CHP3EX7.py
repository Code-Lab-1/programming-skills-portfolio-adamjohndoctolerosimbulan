#Adding values to a variable
lugar = ["South Korea", "Japan", "Canada", "North Pole", "France"]

#Printing the original sequence of the list
print("\nOriginal sequence:")
print(lugar)

#Printing the alphabetical sequence of the list
print("\nAlphabetical:")
print(sorted(lugar))

#Printing the original sequence of the list
print("\nOriginal sequence:")
print(lugar)

#Using the sorted function and printing the reversed sequence of the list
print("\nReversed alphabetical:")
print(sorted(lugar, reverse=True))

#Printing the original sequence of the list
print("\nOriginal sequence:")
print(lugar)

#Printing the reversed sequence of the list
print("\nReversed:")
lugar.reverse()
print(lugar)

#Printing the reversed sequence of the list back to the original
print("\nOriginal sequence:")
lugar.reverse()
print(lugar)

#Printing the alphabetical sequence of the list
print("\nAlphabetical")
lugar.sort()
print(lugar)

#Printing the reversed alphabetical sequence of the list
print("\nReverse alphabetical")
lugar.sort(reverse=True)
print(lugar)