
"""
Tic Tac Toe Player
"""

import math
import copy

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
    Counter_X = 0
    Counter_0 = 0
    if board == initial_state():
        return X

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                Counter_X += 1
            elif board[i][j] == O:
                Counter_0 += 1

    if Counter_X > Counter_0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create new board, without modifying the original board received as input
    if action not in actions(board):
        raise Exception("Invalid Action!!!")
    
    
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    # Check how to handle exception when a non terminal board is received.


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = maximum_value(board)
            return move
        else:
            value, move = minimum_value(board)
            return move


    
def minimum_value(board):
    if terminal(board):
        return utility(board), None

    v_so_far = float('inf')
    move = None
    for action in actions(board):
        # v_so_far = max(v_so_far, maximum_value(result(board, action)))
        the_value, the_action = maximum_value(result(board, action))
        if the_value < v_so_far:
            v_so_far = the_value
            move = action
            if v_so_far == -1:
                return v_so_far, move

    return v_so_far, move

def maximum_value(board):
    if terminal(board):
        return utility(board), None

    v_so_far = float('-inf')
    move = None
    for action in actions(board):
        # v_so_far = max(v_so_far, minimum_value(result(board, action)))
        the_value, the_action = minimum_value(result(board, action))
        if the_value > v_so_far:
            v_so_far = the_value
            move = action
            if v_so_far == 1:
                return v_so_far, move

    return v_so_far, move
    
