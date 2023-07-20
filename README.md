# Tic-tac-toe

This game was part of CS50 Introduction to Artificial Intelligence. Now you can play by your own, choosing X or O to play, with a strong opponent.
The algorithm in tictactoe.py to make it possible to play the game agains an AI. Using minmax, the solution checks all the possible boards
playing accordingly to win or, at least, not to loose.
## tictactoe.py
Object with all methods for the AI of the game.
### def initial_state(board):
This function returns a list of lists, each row of the boar is represented as [EMPTY, EMPTY, EMPTY] at the beginning of the game.    
### def player(board):
Def player checks the board and by counting how many times X and O are "printed" in the board, returns who is the player of the round.
### def actions(board):
Actions returns a set() of all the possible actions in the board. As the board is a list of three lists, a action (0,0), for example, represents that the player can play in the first field of the first row. Basically any empty space is an action.
### def result(board, action):
It returns how the board will be after an action. As the board is a matrix, the board can be changed based on x and y information given by actions(board).
### def winner(board):
### def terminal(board):
### def utility(board):
### def max_value(board):
### def min_value(board):
### def minimax(board):

## How to Run

## Versions

