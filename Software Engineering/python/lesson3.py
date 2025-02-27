# Learning about functions
# What are functions in programming?
# Functions are a block of reusable code that only runs when it is called.
# You can pass data, known as parameters or arguements, into a function.
# A function can return data as a result.
# Functions help to organize and modularize code.

# How to define a function in Python
# In Python, you define a function using the "def" keyword.
def my_function():
    print("Hello from a function")

# How to call a function in Python
# To call a function, simply write the function name followed by parentheses.
my_function()

def greetings(user_name):
    return (f"Hello {user_name}")

print(greetings("John"))

# Calculate the area of a circle

import math

def area_of_circle(radius):
    return math.pi * radius ** 2

print(area_of_circle(int(input("Enter the radius of the circle: "))))


# not using math module
def area_of_circle(radius):
    return 3.14 * radius ** 2    