# Chapter 6, Exercise 5: No Pastrami

# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.

# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
sandwich_orders = [
    'pastrami', 'pastrami', 'BLT', 'pastrami',
    'BLT', 'Philly Steak', 'pastrami']
finished_sandwiches = []

# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
print("\tI'm so sorry, we're all out of pastrami today. We cannot proceed with your order.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " Sandwich.")
    finished_sandwiches.append(current_sandwich)

# Make sure no pastrami sandwiches end up in finished_sandwiches.
print("\n")
for sandwich in finished_sandwiches:
    print("I made your " + sandwich + " Sandwich.")
