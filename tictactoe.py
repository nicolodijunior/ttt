"""
Tic Tac Toe Player
"""

import math
import copy
import time


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    """
    The player function should take a board state as input, and return which player’s turn it is (either X or O).

    In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).

    """
    # Check the number of X and O on the board

    """
    BOARD IS:
            [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    """
    x = 0
    o = 0

    for y in range(3):
        for z in range(3):
            if board[y][z] == X:
                x+=1
            if board[y][z] == O:
                o+=1
    
    if x > o:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    """
    The actions function should return a set of all of the possible actions that can be taken on a given board.

    Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    Possible moves are any cells on the board that do not already have an X or an O in them.
    Any return value is acceptable if a terminal board is provided as input.

    """
    # Return all empty cells as possible moves

    possible_moves = set()

    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                possible_moves.add((r,c))
    
    return possible_moves   


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    """
    The result function takes a board and an action as input, and should return a new board state, without modifying the original board.

    If action is not a valid action for the board, your program should raise an exception.
    The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
    Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.

    """

    new_board = copy.deepcopy(board)

    round_player = player(board)
    try:
        i = action[0]
        j = action[1]
    except:
        raise Exception("Invalid move")
    
    if i > 2 or j > 2:
        raise Exception("Invalid move")
    
    new_board[i][j] = round_player

    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    """
    The winner function should accept a board as input, and return the winner of the board if there is one.

    If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
    One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
    If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.

    """

    for r in range(3):
        if board[r][0] == X and board[r][1] == X and board[r][2] == X:
            return X
        if board[r][0] == O and board[r][1] == O and board[r][2] == O:
            return O
    
    for c in range(3):
        if board[0][c] == X and board[1][c] == X and board[2][c] == X:
            return X
        if board[0][c] == O and board[1][c] == O and board[2][c] == O:
            return O
        
    
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    return None

            



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    """
    The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.

    If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
    Otherwise, the function should return False if the game is still in progress.

    """
    if winner(board) == X or winner(board) == O:
        return True
    if len(actions(board)) == 0:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    """
    The utility function should accept a terminal board as input and output the utility of the board.

    If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
    You may assume utility will only be called on a board if terminal(board) is True.
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    
    return 0

def max_value(board):

    if terminal(board):
        return utility(board)  
     
    max_uty = -2

    for act in actions(board):
        if utility(board) == 1:
            max_uty = 1
            break
        max_uty = max(max_uty, min_value(result(board, act)))
    
    return max_uty


def min_value(board):
    if terminal(board):
        return utility(board)
    min_uty = +2

    for act in actions(board):
        if utility(board) == -1:
            min_uty = -1
            break
        min_uty = min(min_uty, max_value(result(board, act)))
    
    return min_uty

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    """
    The minimax function should take a board as input, and return the optimal move for the player to move on that board.

    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the minimax function should return None.

    """


    if terminal(board):
        return None    
    


    best_act = None
    best_uty = -2
    for act in actions(board):
        new_board = result(board, act)
        mv = min_value(new_board)
        print(act, mv)
        if mv > int(best_uty):
            best_uty = mv
            best_act = act


    print(best_act)
    print("---------------")
    return best_act
    
