# Chapter 1, Exercise 3: Print date and Time


#Display the current date and time
import datetime
now = datetime.datetime.now()
print ("Current date and time : 2023 , 1, 6, 15, 8, 24, 78915 ")
print (now.strftime("%Y-%m-%d %H:%M:%S")) 
