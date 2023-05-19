# **Guess Number Game**

![Guess Number Game]()

This is a simple game that is created using python and run in the Terminal. The user is asked to add a name and after adding name the user decides whether to play the game or not by tying(yes/no). The user has three chances to guess the number. The user will win the game if find the number using three chances otherwise the user will lose.
 
Link to deployed project- 

## How to play

To play this game you need to add a name and after adding the name you will be asked if you want to play the game or not. If you type anything other than(yes/no). The message "Sorry I don't undrestand that." will appear.
If yes then the game starts and the user has three chances to guess the number. If the user guess is higher than the number the message "Guess lower" will help user to guess lower to find the number and if the user guess is lower the message "Guess higher" will help user to find number. The player will win this game if find the number using three chances otherwise will lose and will be asked if wanted to play again.

## Current Features

+ Accpets user input
+ Reads user input
+ Validate input
+ Rising errors
+ Manipulate data

The user inputs are validated and if the user add any invalid input then the feedback is provided to let the user realize where the problem is.
In case if the user failed and wanted to play again can start the game again by typing answer yes(Do you want to play again?).

## Design

**Colours**
+ inputs - BLUE
![inputs colours]()

+Errors and failed message - RED
![Errors]()

+ play game questions and guess higher and lower - yellow
![yellow texts]()






## Creating the Heroku app

When you create the app, you will need to add two build packs from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

