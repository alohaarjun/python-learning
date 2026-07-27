import random

def quiz():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = input(f"What is {a} + {b}? ")  # Using f-strings for cleaner formatting
    if c == str(a + b):
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The answer is {a + b}.")
        return 0

# Using a loop instead of repeating function calls
d = sum(quiz() for _ in range(10))
print(f"You got {d} out of 10 correct.")
if d > 8:
    print("You are an addition master!")
else:
    print("Keep practicing!")
