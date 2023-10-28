# Chapter 1, Exercise 5: Compute area of Circle

# Write a Python program which accepts the radius of a circle from the user and compute the area.
#Area of circle

def findArea(r):
   PI = 3.142
   return PI * (r*r);
   
# Driver method
print("Area is %.6f" % findArea(10));
