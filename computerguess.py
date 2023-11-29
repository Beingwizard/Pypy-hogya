import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #this could be high b/c low = high
        feedback = input(f'Is {guess} too high(h), too low(l) or correct(c)')
        if feedback== 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay, the computer has guessed the correct number {guess}.")

computer_guess(1000)