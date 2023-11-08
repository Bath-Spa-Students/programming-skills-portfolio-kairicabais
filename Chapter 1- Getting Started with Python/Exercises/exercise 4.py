# Chapter 1, Exercise 4: Strings Concatination

#Three strings in different variables added together with the help of string concantination (+) or (,)
a = "How"
b = " are"
c = " you?"
d= a + b + c
print(d)


x = 10
y = 20
z = 30
a = x + y + z
print(a)


print("Enter Marks Obtained in 5 Subjects: ")
mOne = int(input())
mTwo = int(input())
mThree = int(input())
mFour = int(input())
mFive = int(input())

sum = mOne+mTwo+mThree+mFour+mFive
avg = sum/5
perc = (sum/500)*100

print(end="Average Mark = ")
print(avg)
print(end="Percentage Mark = ")
print(perc)