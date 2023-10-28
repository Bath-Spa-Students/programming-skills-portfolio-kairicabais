# Chapter 4, class practise 3: Simple Calculater User input

# Conditional if-elif-else simple calculator with user input. My calculator lacks decimal input.
num1 = input("First Number:\n")
operator = input("Operator (+, -, *, /):\n")
num2 = input("Second Number:\n")

num1 = float(num1)
num2 = float(num2)

out = None

if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2
    
print("Answer: " + str(out))
