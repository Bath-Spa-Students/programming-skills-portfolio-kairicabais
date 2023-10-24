# Exercise 5: Change Guest List

#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
#Change list, invite someone else:


#1•Start with your program from Exercise 3-4.
guests = ['Mr. Marco Bucci', 'Ms. Amala Dlamini', 'Mr. Damini Ogulu']



# Add a print() call at the end of your program 'stating the name of the guest who can’t make it'.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

#notice a guest will not be coming.

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")



#2•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

## Ms. Amala sadly couldn't make it, so I invite Mr. Mark Merchant in her place. 
del(guests[1])
guests.insert(1, 'Mark Merchant')



#•Print a second set of invitation messages, one for each person who is still in your list.
name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")
