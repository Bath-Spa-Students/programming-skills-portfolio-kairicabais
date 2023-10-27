# Chapter 5, Exercise 2: Glossary (a.k.a PYTHON DICTIONARY)

# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# * Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'String Concatenation': 'a plus(+) or comma(,) sign that add strings together.',
    'integer': "A “container” that can store any kind of value.",
    }

# * Print each word and its meaning as neatly formatted output. 
# print the word followed by a colon and then its meaning, 
word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'String Concatenation'
print("\n" + word.title() + ": " + glossary[word])

word = 'integer'
print("\n" + word.title() + ": " + glossary[word])



# or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
word = 'string'
print("\n" + word.title())
print(glossary[word])

word = 'comment'
print("\n" + word.title())
print(glossary[word])

word = 'list'
print("\n" + word.title())
print(glossary[word])

word = 'String Concatenation'
print("\n" + word.title())
print(glossary[word])

word = 'integer'
print("\n" + word.title())
print(glossary[word])
