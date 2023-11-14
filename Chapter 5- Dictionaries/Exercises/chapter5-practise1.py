# Chapter 5, practise 1

# tuple = ()
# list = []
# dict + {} , dictionary displays data as tuple format.

dictionary = {}
print(dictionary)


# (1,2,3) index of 1 is 0, index of 2 is 1, index of 3 is 2
# dictionary stores data in the key + value pair. You cannot chamge keys you can change value. 

# To add something in dictionary
example = {'drinks' : 'bubble tea' ,
           'mall' : 'Dubai Festival Center' ,
           'animal' : 'penguins'}
print(example)



dictionary = {'movie' : 'Barbie' ,
             'no. of times watched' : '2',
              'at age' : '7' }
print(dictionary)
# dictionary print the dictionary keys only
print(dictionary.keys())
# delete dictionary key 'ate age'
del(dictionary['at age'])
del(dictionary['movie'])


# pop items 
watching = {'anime' : 'demon slayer' ,
             'season' : '4',
              'episode' : '104' }
print(watching)
#
print(watching.popitem())
print(watching.keys())
print(watching.values())
