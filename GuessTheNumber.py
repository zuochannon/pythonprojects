import random


def get_num_from_user():
    """ Checks if the user's input is a number between 1 and 100. 
    If it is, it will return the number. If it is not, it will 
    continue to ask the user for another number until it is a number between 1 and 100

    'q' to quit the program

    Returns:
        _int_ : a valid user's guess

    Raises: 
        TypeError: If user's input is not a number between 1 and 100
    """

    num = input(
        "Type 'q' to quit the program.\nGuess a number between 1 and 100: ")

    try:
        if int(num) > 100 or int(num) < 1:
            print("Invalid number. Must be between 1 and 100.\n")
            return get_num_from_user()
        else:
            return int(num)
    except TypeError:
        if num == "q":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Must be between 1 and 100.\n")
            return get_num_from_user()


def main():
    """ Main function to run the program.
    'q' can be used to quit the program."""
    # Randomly generates a number between 1 and 100
    computer_num = random.randint(1, 100)

    # Asks the user for a number between 1 and 100
    user_guess = get_num_from_user()

    # Boolean to check if the user's guess is correct
    num_found = False

    # Counts the number of tries the user took to guess the number
    count = 1

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
        f"Your guess is correct. It was {computer_num}! It took you {count}\
{'tries' if count > 1 else 'try'} to guess the number.")


main()
