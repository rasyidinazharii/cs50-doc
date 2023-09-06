"""
Tic Tac Toe Player
"""

import math

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
    
    raise NotImplementedError


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count <= o_count:
        return X
    else:
        return O
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")
    current_player = player(board)
    new_board = [row.copy() for row in board]
    new_board[action[0]][action[1]] = current_player
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if current_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]

    raise NotImplementedError


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    best_action = None

    for action in actions(board):
        new_board = result(board, action)
        min_val = min_value(new_board)[0]
        if min_val > v:
            v = min_val
            best_action = action

    return v, best_action

    raise NotImplementedError


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    best_action = None

    for action in actions(board):
        new_board = result(board, action)
        max_val = max_value(new_board)[0]
        if max_val < v:
            v = max_val
            best_action = action

    return v, best_action

    raise NotImplementedError





# def player(board):
#     """
#     Returns player who has the next turn on a board.
#     """
#     raise NotImplementedError


# def actions(board):
#     """
#     Returns set of all possible actions (i, j) available on the board.
#     """
#     


# def result(board, action):
#     """
#     Returns the board that results from making move (i, j) on the board.
#     """
#     raise NotImplementedError


# def winner(board):
#     """
#     Returns the winner of the game, if there is one.
#     """
#     raise NotImplementedError


# def terminal(board):
#     """
#     Returns True if game is over, False otherwise.
#     """
#     raise NotImplementedError


# def utility(board):
#     """
#     Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
#     """
#     raise NotImplementedError


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     raise NotImplementedError
