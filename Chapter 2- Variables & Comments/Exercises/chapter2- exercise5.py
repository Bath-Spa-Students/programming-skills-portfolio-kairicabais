# Chapter 2, Exercise 5: USB Shopper 

# A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. 

# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
# You will to use the arithmetic operators to complete this exercise.

# They are £6 each.
usb_cost=6

# she wants to spend only £50.
usb_money=50

total=usb_money/usb_cost
print(total)

# total rounded to the nearest number so we can find out how many usbs the girl can actually buy.
print(round(total))


# for divison below:
total_usb=usb_money//usb_cost

# Using string concatenation, we can print our sentence and 
change=usb_money%total_usb
print("The amount of usbs you can buy with " + str(usb_money) + " is " + str(total_usb) + " and the change is $" + str(change))
