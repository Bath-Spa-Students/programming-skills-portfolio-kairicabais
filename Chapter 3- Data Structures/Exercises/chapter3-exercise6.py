# Exercise 6: Shrinking Guest List


#My guests from previous list that can come.
guests= ['Mr. Marco Bucci', 'Mr. Mark Merchant', 'Mr. Damini Ogulu']

#you have space for only two guests. So I will apologize to one of my guests.
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")



# •Print a message to each of the two people still on your list, letting them know they’re still invited.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Now my list is empty.
print(guests)