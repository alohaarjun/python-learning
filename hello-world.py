# This is a comment. Comments are ignored by Python.
# They are used to explain what the code does.

# Print a message to the screen
print("Hello, World!")

# Variables store information that can be used later
name = "Arjun"  # This is a string variable
age = 11  # This is an integer variable

# Print the values of the variables
print("My name is", name)
print("I am", age, "years old")

# Simple arithmetic operations
sum = 5 + 3  # Addition
difference = 10 - 2  # Subtraction
product = 4 * 2  # Multiplication
quotient = 16 / 2  # Division

# Print the results of the arithmetic operations
print("5 + 3 =", sum)
print("10 - 2 =", difference)
print("4 * 2 =", product)
print("16 / 2 =", quotient)

# Using an if statement to make decisions
if age > 10:
    print("You are older than 10 years old!")
else:
    print("You are 10 years old or younger.")

# A simple loop to repeat actions
for i in range(5):
    print("This is loop iteration number", i)

# A function that takes two arguments and returns their sum
def add_numbers(a, b):
    return a + b

# Call the function and print the result
result = add_numbers(3, 4)
print("The sum of 3 and 4 is", result)

# A list of numbers
numbers = [1, 2, 3, 4, 5]

# Loop through the list and print each number
for number in numbers:
    print(number)

# A dictionary of names and ages
ages = {"Alice": 25, "Bob": 30, "Charlie": 35}

# Loop through the dictionary and print each name and age
for name, age in ages.items():
    print(name, "is", age, "years old")

# A class that represents a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

# Create a person object and call the greet method
person = Person("David", 40)
person.greet()

# Import a module and use a function from it
import math

result = math.sqrt(16)
print("The square root of 16 is", result)

# Import a module and use a class from it
from datetime import datetime

now = datetime.now()
print("The current date and time is", now)
 