#Assigning the glossary to a variable
glossary = {
    'print': 'The print() function prints the specified message to the screen.',
    'variables': 'Variables are containers for storing data values.',
    'booleans': 'Booleans represent one of two values: True or False.',
    'tuple': "Tuples are used to store multiple items in a single variable.",
    'list': 'A collection of items in a particular order.',
    }
#Prints the title and term
term = 'print'
print(f"\n{term.title()}: {glossary[term]}")

term = 'variables'
print(f"\n{term.title()}: {glossary[term]}")

term = 'booleans'
print(f"\n{term.title()}: {glossary[term]}")

term = 'tuple'
print(f"\n{term.title()}: {glossary[term]}")

term = 'list'
print(f"\n{term.title()}: {glossary[term]}")