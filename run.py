
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




# Write your code to expect a terminal of 80 characters wide and 24 rows high
