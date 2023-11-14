# chapter4, class practise 1 example of control structures


# this is an example of a simple structure
bubble_tea = float(input("Enter amount of bubble teas: "))
bonus = 0

# i will make an example mimicking a buy 1 get 1 free offer in a  bubble tea shop. 
if bubble_tea > 1 :
    bonus = 1
else:
    bonus = 0

# This will make the show if the offer is applicable, that we can get a bonus bubble tea if we buy more than 1 bubble tea. 
print("Your Bonus: "+str(bonus))
