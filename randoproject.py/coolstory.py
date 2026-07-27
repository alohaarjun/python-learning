import random
fn = random.randint(1,20)
sn = random.randint(1,20)
try:
    user_input = int(input(f"What is {fn} times {sn}? "))
    if fn * sn == user_input:
        print("Correct!")
    else:
        print("Incorrect! The answer is", fn * sn)
except ValueError:
    print("Sorry, that is not a valid input. Please enter a number.")