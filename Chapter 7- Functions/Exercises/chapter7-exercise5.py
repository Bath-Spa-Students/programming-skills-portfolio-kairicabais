# Chapter 7, Exercise 5: Cities


# Write a function called describe_city() that accepts the name of a city and its country. 
# Give the parameter for the country a default value.


def describe_city(city, country='The Philippines'):
    """Describe a city."""
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

# Call your function for three different cities, at least one of which is not in the default country. 
describe_city('Olongapo')
describe_city('Reykjavik', 'Iceland')
describe_city('Manila')
describe_city('Surigao')
describe_city('Cagayan De Oro')
