# Making an empty list
pets = []

#Adding informations to the variables
pet = {
    'Animal type': 'Dog',
    'Name': 'Motmot',
    'Owner': 'Esmei',
    'Color': 'White',
}
pets.append(pet) #Places new items

pet = {
    'Animal type': 'Cat',
    'Name': 'Meowy',
    'Owner': 'Kim',
    'Color': 'Black',
}
pets.append(pet) #Places new items

pet = {
    'Animal type': 'Hamster',
    'Name': 'Bernie',
    'Owner': 'Ralph',
    'Color': 'Brown',
}
pets.append(pet) #Places new items

pet = {
    'Animal type': 'Fish',
    'Name': 'Juan',
    'Owner': 'Apple',
    'Color': 'Orange',
}
pets.append(pet) #Places new items

pet = {
    'Animal type': 'Rat',
    'Name': 'Remy',
    'Owner': 'Adam',
    'Color': 'Gray',
}
pets.append(pet) #Places new items

# Displays information about the pets listed above
for pet in pets:
    print(f"\nHere's what I know about {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")