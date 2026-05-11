import random

# Generate a random number between 1 and 100
num = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")

while True:
    # Get user input and convert to integer
    try:
        guess = int(input('Guess a random number from 1 to 100: '))
        attempts += 1

        if guess > num:
            print('Too high for the number')
        elif guess < num:
            print('Too low for the number')
        else:
            print(f'Correct! You guessed it in {attempts} tries.')
            break  # End the loop when guessed correctly
            
    except ValueError:
        print("Please enter a valid whole number.")
