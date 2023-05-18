import random

def greet_user(name): # function to greet user
    if not username.isalpha():
        # I need to return back here and check username
        print("Name cannot be a number.")
    elif len(username) < 3:
        print("Name should be at least three letters.")
    elif len(username) > 30:
        print("User name cannot be more than 15 letters.")
    else:
        print("Welcome!")
        print(f"Hello {username}, Lets play a game.")
username = input("Add Name: ") # input for username
greet_user(username)
play_game = input("Do you want to play game?(yes/no) ").lower()
number = random.randint(0, 100)
number_of_guesses = 0
guess_limit = 3

def start_playing():
    print("Game started!")
    if number_of_guesses < guess_limit:
        guess = int(input("Guess a number: "))








