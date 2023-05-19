import random
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

username = input(f"{Fore.BLUE}Add Name: ") # input for username


def greet_user():
    """
    Check if the name is valid.
    Greet user using username.
    """ 
    if not username.isalpha():
        # I need to return back here and check username
        print("Please add a valid name.")
    elif len(username) < 3:
        print("Name should be at least three letters.")
    elif len(username) > 30:
        print("User name cannot be more than 30 letters.")
    else:
        print(f"{Fore.YELLOW}Welcome!")
        print(f"Hello {username}, Lets play a game.")


greet_user()
play_game = input(f"{Fore.YELLOW}Do you want to play game?(yes/no) ").lower()
number = random.randint(0, 100)
number_of_guesses = 0
guess_limit = 3


def start_playing(): # function to start the game
    print(f"{Fore.GREEN}Game started!")
    global number_of_guesses
    while number_of_guesses < guess_limit:

        try: # check if the user enters a number
            guess = int(input(f"{Fore.BLUE}Guess a number: "))
            number_of_guesses += 1
        except ValueError:
            print(f"{Fore.RED}Invalid: You are told to guess a number.")
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
            break          
    else:
        """
        If the user guessed three numbers and couldn't find the right number
        The message you failed will display
        Ask the user if the user wanted to play again
        """
        print(f"{Fore.RED}{username} You Failed!")
        play_again = input(f"{Fore.YELLOW}Do you want to play again?(yes/no) ").lower()
        if play_again == "yes":
            number_of_guesses = 0
            start_playing()
        else:
            print(f"{Fore.RED}Quit")
        
        
if play_game == "yes":
    start_playing()
elif play_game == "no":
    print("Quiet")
else:
    # If the user enter anything other than(yes/no), the this message will display.
    print(f"{Fore.RED}Sorry I don't undrestand that.")








