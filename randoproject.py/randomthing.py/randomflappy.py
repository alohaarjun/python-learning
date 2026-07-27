import random 

# function to safely get a valid guess
def get_valid_guess(prompt):
    while True:
        try:
            guess = int(input(prompt))
            if 1 <= guess <= 20:
                return guess
            else:
                print("That’s not between 1 and 20! Try again.")
        except ValueError:
            print("That’s not a number! Try again.")

# Explain the game
print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 20.")
print("You have up to 5 tries to guess it.")  # corrected from 6 to 5
print("After each guess, I’ll tell you if your guess is too high or too low.")

tries = 0
a = random.randint(1, 20)

# first guess
guess = get_valid_guess('Guess a number between 1 and 20: ')

# guessing loop
while guess != a and tries < 5:
    tries += 1
    if guess < a:
        guess = get_valid_guess('Too low! Try again: ')
    else:
        guess = get_valid_guess('Too high! Try again: ')

# end messages
if guess == a:
    print('You guessed it! The number was ' + str(a))
else:
    print('You weren\'t able to guess the number in time! The number was ' + str(a))w