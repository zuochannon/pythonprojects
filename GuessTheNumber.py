import random


def get_num_from_user():
    """ Checks if the user's input is a number between 1 and 100. 
    If it is, it will return the number. If it is not, it will 
    continue to ask the user for another number until it is a number between 1 and 100

    'q' to quit the program

    Returns a valid user's guess
    """

    num = input(
        "Type 'q' to quit the program.\n Guess a number between 1 and 100: ")

    try:
        if int(num) > 100 or int(num) < 1:
            print("Invalid number. Must be between 1 and 100.\n")
            return get_num_from_user()
        else:
            return int(num)
    except Exception:
        try:
            if num == "q":
                print("Goodbye!")
                exit()
            else:
                print("Invalid input. Must be between 1 and 100.\n")
                return get_num_from_user()
        except Exception:
            print("Unknown error.")
            exit()


def main():
    # Randomly generates a number between 1 and 100
    computer_num = random.randint(1, 100)

    # Asks the user for a number between 1 and 100
    user_guess = get_num_from_user()

    # Boolean to check if the user's guess is correct
    num_found = False

    # Counts the number of tries the user took to guess the number
    count = 1

    '''
    This while loop will continue to ask the user for another number until the user guesses the correct number.
    Unless the user quits the program, the program will end.'''
    while not num_found:
        if user_guess > computer_num:
            print("Your guess is too high.\n")
            count += 1
            user_guess = get_num_from_user()
        elif user_guess < computer_num:
            print("Your guess is too low.\n")
            count += 1
            user_guess = get_num_from_user()
        else:
            num_found = True

    print(
        f"Your guess is correct. It was {computer_num}! It took you {count} {'tries' if count > 1 else 'try'} to guess the number.")


main()
