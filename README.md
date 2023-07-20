# Tic-tac-toe

This game was part of CS50 Introduction to Artificial Intelligence. Now you can play by your own, choosing X or O to play, with a strong opponent.
The algorithm in tictactoe.py makes it possible to play the game against an AI. Using minimax, the solution checks all the possible boards,
playing accordingly to win or, at least, not to lose.


## Table of Contents

- [Code](#tictactoe.py)
- [Installation](#installation)
- [Credits](#credits)
- [License](#license)
- [Video}(#video)

## tictactoe.py
Object with all methods for the AI of the game.
### def initial_state(board):
This function returns a list of lists, each row of the boar is represented as [EMPTY, EMPTY, EMPTY] at the beginning of the game.    
### def player(board):
Def player checks the board and by counting how many times X and O are "printed" in the board, returns who is the player of the round.
### def actions(board):
Actions returns a set() of all the possible actions in the board. As the board is a list of three lists, an action (0,0), for example, represents that the player can play in the first field of the first row. Basically, any empty space is an action.
### def result(board, action):
It returns how the board will be after an action. As the board is a matrix, the board can be changed based on x and y information given by actions(board).
### def winner(board):
The winner function should accept a board as input, and return the winner of the board if there is one. It is made by checking the horizontal, vertical, and diagonal possible ways to win.
### def terminal(board):
The terminal function accepts a board as input and returns a boolean value indicating whether the game is over. If there is a winner or there are no more empty spaces, it returns True.
### def utility(board):
Using winner(board), the utility returns 1 if X has won the game, -1 if O has won, and 0 otherwise.
### def max_value(board):
This recursive method returns the best option for player X, considering the best option between all the boards after the opponent's turn, by calling min_value and checking the bigger value between the 2. When the board is a terminal board, it returns its utility. Using recursion, the method checks all possible games starting with the first board provided.
### def min_value(board):
This method works exactly like max_value, but it starts with the minimum option for the player X, and checks the lower value between all the boards, considering the opponent will make the best move it can.
### def minimax(board):
Minimax returns None if the board is a terminal board, there is a winner or there is no space for a next move. If the player is X, the AI maximizes the utility by calling min_value for each action possible in the next round and checking for which X benefits are bigger. If the player is O, as utility returns 1 if X wins in a board, minimax checks the lower value between all boards, considering that the next move X will do is to maximize its own result.


## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository to your local machine using the following command:
   git clone https://github.com/nicolodijunior/ttt.git
3. cd cs50-ai-tictactoe   
4. pip install -r requirements.txt
5. Run python runner.exe on your terminal

## Credits
This project is a part of the CS50 Introduction to Artificial Intelligence with Python course offered by Harvard University. The implementation of the minimax algorithm and the game's structure are inspired by the course materials.

## License
This course is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. This is a human-readable summary of (and not a substitute for) the [license](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode). More information [here](https://cs50.harvard.edu/ai/2020/license/).

## Video

   


