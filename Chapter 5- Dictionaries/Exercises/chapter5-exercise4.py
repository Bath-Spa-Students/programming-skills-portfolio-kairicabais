# Chapter 5, Exercise 4: Rivers

# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
rivers = {
    'Rhine': 'Switzerland',
    'Wailua': 'United States',
    'Yangtze': 'China',
    'Rio Grande de Mindanao': 'Philippines',
    'Amazon': 'Brazil',
    }



#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river, country in rivers.items():
    print("The " + "River " + river.title() + " flows through " + country.title() + ".")

#* Use a loop to print the name of each river included in the dictionary.
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())


#* Use a loop to print the name of each country included in the dictionary.
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
