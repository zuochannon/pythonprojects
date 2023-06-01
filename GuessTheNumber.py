import random
def get_num_from_user():
    num = input("Guess a number between 1 and 100: ")
    try:
        if int(num) > 100 or int(num) < 1:
            raise ValueError("Invalid number. Must be between 1 and 100.")
        
    

def main():
    computer_choice = random.randint(1, 100)
    guessed_num = False
    user_guess = int(input("Guess a number between 1 and 100: "))
    while not guessed_num:
        prev_guessed_num = user_guess
        try:
            if int(user_guess) == computer_choice:
                guessed_num = True
            elif int(user_guess) > computer_choice:
                print("Your guess is too high.")
                user_guess = int(
                    input(f"Guess a number between 1 and {prev_guessed_num - 1}: "))
                continue
            else:
                print("Your guess is too low.")
                user_guess = int(
                    input(f"Guess a number between {prev_guessed_num + 1} and 100: "))
                continue
        except ValueError:
            if user_guess == "q":
                print("Goodbye!")
                break
            else:
                print("Invalid input.")
                user_guess = int(
                    input(f"Guess a number between 1 and 100: "))
    print("You guessed the number!")
    print("The number was", computer_choice)


main()
