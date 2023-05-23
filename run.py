import random
import colorama
from colorama import Fore, Style
import sys
colorama.init(autoreset=True)


def greet_user():  # Greet user using username.
    print(f"{Fore.YELLOW}Welcome to Guess Number Game!")
    print("Lets find the secret number.")


greet_user()


def validate_username():
    """
    Checks if the name is valid or invalid\n
    If the name was less then 3 letters or\n
    or more than 30 letters the user will be asked\n
    to write a valid name.\n
    """
    while True:
        username = input(f"{Fore.BLUE}Add Name: ").capitalize()
        if len(username) < 3:
            print(f"{Fore.RED}Name should be at least three letters")
            continue
        elif len(username) > 30:
            print(f"{Fore.RED}Name cannot be more than 30 letters.")
            continue
        else:
            print(f"Hello {username}, lets find the secret number.")
            print(f"{username}, you have three chances to find the number.")
            return username
            break


username = validate_username()

number = random.randint(0, 101)
number_of_guesses = 0
guess_limit = 3


def start_playing(username):  # function to start the game
    print(f"{Fore.GREEN}Game started!")
    global number_of_guesses
    while number_of_guesses < guess_limit:

        try:  # check if the user enters a number
            guess = int(input(f"{Fore.BLUE}Guess a number: "))
            number_of_guesses += 1
        except ValueError:
            print(f"{Fore.RED}Invalid: Please write a number.")
            continue
        """
        check if the guess is lower or higher the number.
        Tell the user to guess lower or higher to find the number.
        """
        if guess > number:
            print(f"{Fore.YELLOW}Guess lower!")
        elif guess < number:
            print(f"{Fore.YELLOW}Guess higher!")
        else:
            print(f"{Fore.GREEN}Hey {username} You won!")
    else:
        """
        If the user guessed three numbers and couldn't find the right number
        The message you failed will display
        Ask the user if the user wanted to play again
        """
        print(f"{Fore.RED}{username} You Failed!")
        play_again = input("Do you want to play again?(yes/no) ").lower()
        if play_again == "yes":
            number_of_guesses = 0
            start_playing(username)
        elif play_again == "no":
            sys.exit("You said no to play again.")
        else:
            print(f"{Fore.RED}Sorry, I don't undrestand '{play_again}'.")


while True:
    play_game = input("Do you want to play game?(yes/no) ").lower()

    if play_game == "yes":
        start_playing(username)
    elif play_game == "no":
        sys.exit("You said no to play game!")
    else:
        # Anything else instead of yes/no in play_game input
        print(f"{Fore.RED}Sorry, I don't undrestand '{play_game}'.")
        continue
