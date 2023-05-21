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

## Technologies Used

### Languages Used
+ Python

### Python Libraries Used

+ [random](https://docs.python.org/3/library/random.html) for integer number 
+ [Clorama](https://pypi.org/project/colorama/) for printing colorful texts


### Python Packages
+ Colorama Text in the terminal are shown in different colors.
+ Random returns a random integer

### Tools 
+ Heroku 


## Content

The content is written by author.

## Fixed Bugs

+ I imported and installed Colorama to add color to the texts. But the text was not in a different color I returned and check my codes if I had truly imported and installed Colorama. The issue was solved by installing the Colorama (pip install Colorama). The reason was that I had closed my workspace and opened a new one instead of opening the previous one.
+  


## Acknowledgements

For inspiration in general and advice, I would like to thank my mentor at Code Institute(Maritna Terlevic).

