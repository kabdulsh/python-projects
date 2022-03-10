import random

maximum_number = int(input('How high do you want to guess?\n'))

random_number = random.randint(1, maximum_number)

guess = int(input('What is your first guess?\n'))

if guess < random_number:
    print('Your guess was too low. Guess again.')
elif guess > random_number:
    print('Your guess was too high. Guess again.')
elif guess == random_number:
    print('Correct!')
    
if guess != random_number:
    
    guess = int(input('What is your second guess?\n'))
    
    if guess < random_number:
        print('Your guess was too low. Guess again.')
    elif guess > random_number:
        print('Your guess was too high. Guess again.')
    elif guess == random_number:
        print('Correct!')

if guess != random_number:

    guess = int(input('What is your third guess?\n'))

    if guess < random_number:
        print('Your guess was too low. Guess again.')
    elif guess > random_number:
        print('Your guess was too high. Guess again.')
    elif guess == random_number:
        print('Correct!')

if guess != random_number:

    guess = int(input('What is your fourth guess?\n'))

    if guess < random_number:
        print('Your guess was too low. Guess again.')
    elif guess > random_number:
        print('Your guess was too high. Guess again.')
    elif guess == random_number:
        print('Correct')

if guess != random_number:

    guess = int(input('What is your fifth guess?\n'))
    
    if guess < random_number:
        print('Your guess was too low. Guess again.')
    elif guess > random_number:
        print('Your guess was too high. Guess again.')
    elif guess == random_number:
        print('Correct!')

if guess != random_number:

    guess = int(input('What is your sixth guess?\n'))

    if guess < random_number:
        print('Your guess was too low. Guess again.')
    elif guess > random_number:
        print('Your guess was too high. Guess again.')
    elif guess == random_number:
        print('Correct!')

if guess != random_number:

    guess = int(input('What is your seventh guess?\n'))

    if guess < random_number:
        print('Your guess was too low. Guess again.')
    elif guess > random_number:
        print('Your guess was too high. Guess again.')
    elif guess == random_number:
        print('Correct!')

if guess != random_number:

    guess = int(input('What is your eighth guess?\n'))

    if guess < random_number:
        print('Your guess was too low. Guess again.')
    elif guess > random_number:
        print('Your guess was too high. Guess again.')
    elif guess == random_number:
        print('Correct')

if guess != random_number:

    guess = int(input('What is your ninth guess?\n'))

    if guess < random_number:
        print('Your guess was too low. Guess again.')
    elif guess > random_number:
        print('Your guess was too high. Guess again.')
    elif guess == random_number:
        print('Correct!')

if guess != random_number:

    guess = int(input('What is your tenth guess?\n'))

    if guess < random_number:
        print('Your guess was too low. Guess again.')
    elif guess > random_number:
        print('Your guess was too high. Guess again.')
    elif guess == random_number:
        print('Correct!')

print('The random number was actually %d.' % random_number)