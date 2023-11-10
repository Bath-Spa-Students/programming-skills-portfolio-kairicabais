


# list with integer elements
list =  [5, 20, 15, 20, 25, 50, 20]

# number (n) to be removed
n = 20

# print original list 
print ("Original list:")
print (list)

# loop to traverse each element in list
# and, remove elements 
# which are equals to n
for k in list:
    if k == n:
        list.remove(k)

# print list after removing given element
print ("list after removing elements:")
print (list)
