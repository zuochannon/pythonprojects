import random


def get_num_from_user():
    num = input("Guess a number between 1 and 100: ")
    try:
        if int(num) > 100 or int(num) < 1:
            # TODO: Delete 2 print statements
            print("\n\nINSIDE OF OUT OF RANGE.")
            print("Number out of range.\n\n")

            print("Invalid number. Must be between 1 and 100.")
            get_num_from_user()
        else:
            # TODO: Delete 1 print statement
            print("\n\nYOU DID IT. NO ERRORS.")
            print("returning " + num + "\n\n")

            return int(num)
    except ValueError:
        try:
            if num == "q":
                print("Goodbye!")
                exit()
            else:
                # TODO: Delete 1 print statement
                print("\n\nINPUT A LETTER OTHER THAN 'q'.\n\n")

                print("Invalid input. Must be between 1 and 100.")
                get_num_from_user()
        except ValueError:
            print("Unknown error.")
            exit()

    # print("\n\n ==== DEBUG: " + str(num) + "====\n\n")
    # if num > 100 or num < 1:
    #     print("Number out of range. Must be between 1 and 100.")
    #     get_num_from_user()
    # else:
    #     while not num.isdigit():
    #         if num == "q":
    #             print("Goodbye!")
    #             exit()
    #         else:
    #             get_num_from_user()


def main():
    computer_num = random.randint(1, 100)
    try:
        user_guess = get_num_from_user()
    finally:

        print("\n\n==== DEBUG 2: " + str(user_guess) + "====\n\n")
        while user_guess != computer_num:
            if user_guess > computer_num:
                print("Your guess is too high.")
                user_guess = get_num_from_user()
            elif user_guess < computer_num:
                print("Your guess is too low.")
                user_guess = get_num_from_user()
            else:
                print(
                    f"Your guess is correct. It was {computer_num} and you guessed {user_guess}!")
# def main():
#     computer_choice = random.randint(1, 100)
#     guessed_num = False
#     user_guess = int(input("Guess a number between 1 and 100: "))
#     while not guessed_num:
#         prev_guessed_num = user_guess
#         try:
#             if int(user_guess) == computer_choice:
#                 guessed_num = True
#             elif int(user_guess) > computer_choice:
#                 print("Your guess is too high.")
#                 user_guess = int(
#                     input(f"Guess a number between 1 and {prev_guessed_num - 1}: "))
#                 continue
#             else:
#                 print("Your guess is too low.")
#                 user_guess = int(
#                     input(f"Guess a number between {prev_guessed_num + 1} and 100: "))
#                 continue
#         except ValueError:
#             try:
#                 if user_guess == "q":
#                     print("Goodbye!")
#                 break
#             except ValueError:
#                 print("Invalid input.")
#                 user_guess = int(
#                     input(f"Guess a number between 1 and 100: "))
#     print("You guessed the number!")
#     print("The number was", computer_choice)


main()
