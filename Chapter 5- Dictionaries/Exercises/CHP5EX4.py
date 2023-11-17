#Assigning the dictionary to a variable
rivers = {
    'cagayan': 'philippines',
    'amazon': 'south america',
    'ganges': 'india',
    'mekong': 'thailand',
    'danube': 'europe',
    }

#Using for loop and prints the country and data
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

#Using for loop and prints the rivers listed in rivers variable
print("\nThis data collection includes the following rivers:")
for river in rivers.keys():
    print(f"- {river.title()}")

#Using for loop and prints the countries listed in rivers variable
print("\nThis data collection includes the following countries:")
for country in rivers.values():
    print(f"- {country.title()}")