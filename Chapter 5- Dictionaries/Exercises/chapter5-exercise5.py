# Chapter 5, Exercise 5: Pets 

# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
# A loop uses "append" to add elements to a list. Specifically, the "append" method adds an item to the end of a list.

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'Dog',
    'name': 'Salt',
    'owner': 'Jose',
    'weight': 2,
    'eats': 'Beef Jerky',
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'MingMing',
    'owner': 'Oscar',
    'weight': 3,
    'eats': 'Hotdogs',
}
pets.append(pet)

pet = {
    'animal type': 'Rabbit',
    'name': 'Wenty',
    'owner': 'Teresita',
    'weight': 1,
    'eats': 'Water Spinach',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nEverything I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

