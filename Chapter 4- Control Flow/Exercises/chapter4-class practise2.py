# Chapter 4, practise 2 : The if-else chain

# This is an example of a Nested Decision Structure

# I will make a nested structure that will inform you if you are eligible to buy bubble tea that costs $12.
# I will have two conditions to qualtify you to buy bubble tea: if you have the BUDGET and if you have the CRAVING for bubble tea. 
# if no budget, you will be warned that your funds are insufficent
# if not enough cravings on the cravings scale, you will be advised not to get bubble tea
# only if you qyalify both conditions, you can proceed to get bubble tea!

budget = int(input("Enter your budget:"))
cravings_rating = float(input("On a scale of 1-5, how bad do you want bubble tea: "))

if budget > 12:
 if cravings_rating >=3:
   print ("Congratulations! Go get bubble tea")
 else: 
   print ("You don't crave it enough. Save your money, don't get the bubble tea")
else:
   print ("Unfortunately, you do not have the budget for bubble tea, ")
