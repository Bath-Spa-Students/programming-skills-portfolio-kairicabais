# Chapter 6, Exercise 2: Movie Tickets:

# A movie theater charges different ticket prices depending on a person’s age.
#Write a loop in which you ask users their age, and then tell them the cost of their movie ticket
Movie_tickets = "How old are you?"
Movie_tickets += "\nEnter 'quit' when you are finished. "

while True:
    age = input(Movie_tickets)
    if age == 'quit':
        break
    age = int(age)
# If a person is under the age of 3, the ticket is free; 
if age < 3:
        print("You get in free!")

# if they are between 3 and 12, the ticket is $10;
elif age < 13:     
        print("Your ticket is $10.")
# and if they are over age 12, the ticket is $15. 

else:
        print("Your ticket is $15.")


bruhh = "How old are you?"
bruhh += "\nEnter 'quit' when you are finished. "



while True:
    age = input(bruhh)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")





    age = input("How old are you? ")
    
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif age < 12:
        print("Your ticket is $10") 
    else:
        print("Your ticket is $15")

