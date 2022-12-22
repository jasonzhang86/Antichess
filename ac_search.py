import chess
import random

import ac_global
from ac_exception import *
from ac_evaluation import *

def is_antichess_move(move):
    return ac_global.board.is_capture(move)

def find_all_possible_moves(board_fen):
    """
    Split all possible moves into antichess/regular moves.

    antichess move: moves that capture an opponent's piece, if such a move exists, we must make this move.
    regular move: moves that do not caputure an opponent's piece, we only consider such move if 
                   there is no antichess move
    """
    current_board = chess.Board(board_fen)
    possible_moves = list(current_board.legal_moves)
    antichess_moves = []
    regular_moves = []
    for move in possible_moves:
        if is_antichess_move(move):
            antichess_moves.append(move)
        else:
            regular_moves.append(move)

    if antichess_moves:
        return antichess_moves
    elif regular_moves:
        return regular_moves
    else:
        raise NoLegalAntichessMoveException("Cannot make a valid antichess move.")

def arrange_moves(board_fen, possible_moves):
    """
    An optimation made for tie-breaking moves.

    If there exists multiple moves with the same score, prioritize the promotion moves and the check moves.
    """
    current_board = chess.Board(board_fen)
    promotion_moves = []
    check_moves = []
    regular_moves = []
    for move in possible_moves:
        if move.promotion:
            promotion_moves.append(move)
        elif current_board.gives_check(move):
            check_moves.append(move)
        else:
            regular_moves.append(move)
    random.shuffle(check_moves)
    return promotion_moves + check_moves + regular_moves

def minimax_pruning(board_fen, depth, alpha, beta, maximizingPlayer):
    """
    A recursive function that performs the minimax strategy.

    In each recursive call:
        - If the maximizingPlayer is myself, the function picks a move with the highest position score
        - If the maximizingPlayer is the opponent, the function picks a move with the lowest position score

    alpha and beta are used for pruning.

    depth has to be at least 1. (i.e. we at least consider one step ahead.)
    """ 
    current_board = chess.Board(board_fen)

    # base case
    if depth == 0 or current_board.is_game_over():
        return [evaluation_position(board_fen), "*"]

    possible_moves = find_all_possible_moves(board_fen)

    if maximizingPlayer:
        maxEval = ac_global.INT_MIN
        best_move = None
        improved_possible_moves = arrange_moves(board_fen, possible_moves)

        # If every move in improved_possible_moves places the king in a position that can be checked by opponent's next step,
        # then this method would fail to update maxEval and thus give None as best_move.
        # Therefore we add this check to pick the first move as a placeholder.
        if improved_possible_moves:
            best_move = improved_possible_moves[0]

        for move in improved_possible_moves:
            board = chess.Board(board_fen)
            board.push(move)
            curEval = minimax_pruning(board.fen(), depth-1, alpha, beta, False)[0]
            if curEval > maxEval:
                maxEval = curEval
                best_move = move
            alpha = max(alpha, curEval)
            if beta <= alpha:
                break
        return [maxEval, best_move]

    else:
        minEval = ac_global.INT_MAX
        for move in possible_moves:
            board = chess.Board(board_fen)
            board.push(move)
            curEval = minimax_pruning(board.fen(), depth-1, alpha, beta, True)[0]
            minEval = min(minEval, curEval)
            beta = min(beta, curEval)
            if beta <= alpha:
                break
        return [minEval, "*"]
