choice = ''

while choice != 'quit':

    import random

    choice = input("Would you like to play a GAME, display a SHAPE, or QUIT?\n").lower()

    if choice == 'game':

        print("We shall play a game.\n")

        maximum_number = int(input('How high do you want to guess?\n'))
        user_choice_maximum_number_guesses = int(input('How many guesses would you like to have?\n'))
        random_number = random.randint(1, maximum_number)
        correct_guess = False
        number_of_guesses = 0

        while not correct_guess and number_of_guesses < user_choice_maximum_number_guesses:

            number_of_guesses += 1
            guess = int(input('Guess # {}: ' .format(number_of_guesses)))

            if guess < random_number:

                print('Your guess was too low.\n')

            elif guess > random_number:

                print('Your guess was too high.\n')

            else:
                correct_guess = True
                print('Correct! You got it in {} guesses.\n' .format(number_of_guesses))

        if not correct_guess:
            print('Game over. The correct number was actually {}.\n' .format(random_number))

    elif choice == 'shape':

        print("Which shape would you like to display?\n")
        shape = input("DIAMOND, ISOSCELES TRIANGLE, RECTANGLE, RIGHT TRIANGLE, or SQUARE?\n").lower()

        if shape == "diamond":

            width = 0

            while width < 1 or width > 30:
                width = int(input("Choose a width larger than 1 & smaller than 30.\n"))

            if width % 2 == 0:
                width += 1

            spaces = width // 2
            asterisks = 1

            while asterisks <= width:
                print(" " * spaces, end="")
                print("*" * asterisks)
                spaces -= 1
                asterisks += 2

            spaces += 1
            asterisks -= 2

            while asterisks > 1:
                spaces += 1
                asterisks -= 2

                print(" " * spaces, end="")
                print("*" * asterisks)

        if shape == "isosceles triangle":

            width = 0

            while width < 1 or width > 30:
                width = int(input("Choose a width larger than 1 & smaller than 30.\n"))

            if width % 2 == 0:
                width += 1

            spaces = width // 2
            asterisks = 1

            while asterisks <= width:
                print(" " * spaces, end="")
                print("*" * asterisks)
                spaces -= 1
                asterisks += 2

        if shape == "rectangle":

            length = 0
            width = 0

            while length < 1 or length > 30:
                length = int(input("Choose a length larger than 1 & smaller than 30.\n"))

            while width < 1 or width > 30:
                width = int(input("Choose a width larger than 1 & smaller than 30.\n"))

            for row in range(length):
                print("*" * width)

        if shape == 'right triangle':

            length = 0

            while length < 1 or length > 30:
                length = int(input("Choose a length larger than 1 & smaller than 30.\n"))

            for row in range(1, length + 1):
                print("*" * row)

        if shape == 'square':
            if shape == "square":

                length = 0

                while length < 1 or length > 30:
                    length = int(input("Choose a length larger than 1 & smaller than 30.\n"))

                for row in range(length):
                    print("*" * length)