import random

def greet_user(): # function to greet user
    if not username.isalpha():
        # I need to return back here and check username
        print("Name cannot be a number.")
    elif len(username) < 3:
        print("Name should be at least three letters.")
    elif len(username) > 30:
        print("User name cannot be more than 30 letters.")
    else:
        print("Welcome!")
        print(f"Hello {username}, Lets play a game.")
username = input("Add Name: ") # input for username
greet_user()
play_game = input("Do you want to play game?(yes/no) ").lower()
number = random.randint(0, 100)
number_of_guesses = 0
guess_limit = 3

def start_playing(): # function to start the game
    print("Game started!")
    global number_of_guesses
    while number_of_guesses < guess_limit:
        try:
            guess = int(input("Guess a number: "))
            number_of_guesses += 1
        except ValueError:
            print("Invalid: You are told to guess a number.")
            
    else:
        print(f"{username} You Failed!")
        
        
if play_game == "yes":
    start_playing()
elif play_game == "no":
    print("Quiet")
else:
    print("Sorry I don't undrestand that.")








