#Assigning more glossary to the variable
glossary = {
    'print': 'The print() function prints the specified message to the screen.',
    'variables': 'Variables are containers for storing data values.',
    'booleans': 'Booleans represent one of two values: True or False.',
    'tuple': "Tuples are used to store multiple items in a single variable.",
    'list': 'A collection of items in a particular order.',
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'loop': 'Work through a collection of items, one at a time.',
    'value': 'An item associated with a key in a dictionary.',
    'float': 'A numerical value with a decimal component.',
    }

#Using for loop to print each title and term
for term, meaning in glossary.items():
    print(f"\n{term.title()}: {meaning}")