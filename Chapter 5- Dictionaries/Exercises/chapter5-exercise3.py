# Chapter 5, Exercise 3: Glossary 2 

# Now that you know how to loop through a dictionary, clean up the code by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values.

#loop: Work through a collection of items, one at a time. Loops clean up code, for instance, by replacing your series of print()

# When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.


glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'String Concatenation': 'a plus(+) or comma(,) sign that add strings together.',
    'integer': "A “container” that can store any kind of value.",

# this is the newly added 5 extra words: 

    'input' : "A way to collect the user's input.",
    'value': 'An item that can fall into 3 data types: an integer, float or string.',
    'type casting' : 'A way to assign a specific data type to a variable using functions',
    'variable reassignment' : 'when you give a new variable, the previous assigned variable deletes itself',
    'boolean expression': 'An expression that evaluates to only True or False.',
    }

#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")