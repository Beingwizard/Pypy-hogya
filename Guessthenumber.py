##Guessing the random number provided by the computer.

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too Low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
            
    print(f"Yay, you've guessed the correct number between 1 and {x}")

guess(10)