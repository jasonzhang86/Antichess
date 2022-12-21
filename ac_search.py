import chess
import random

import ac_global
from ac_exception import *
from ac_evaluation import *

def is_antichess_move(move):
    return ac_global.board.is_capture(move)

def find_all_possible_moves(board_fen):
    # split all possible moves into antichess/regular moves
    # :antichess move: moves that capture an opponent's piece, if such a move exists, we must make this move.
    # :regular move: moves that do not caputure an opponent's piece, we only consider such move if 
    #                there is no antichess move
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

def prioritize_check(board_fen, possible_moves):
    current_board = chess.Board(board_fen)
    check_moves = []
    other_moves = []
    for move in possible_moves:
        if current_board.gives_check(move):
            check_moves.append(move)
        else:
            other_moves.append(move)
    random.shuffle(check_moves)
    random.shuffle(other_moves)
    return check_moves + other_moves

def minimax_pruning(board_fen, depth, alpha, beta, maximizingPlayer):
    current_board = chess.Board(board_fen)
    if depth == 0 or current_board.is_game_over():
        return [evaluation_position(board_fen), "*"]

    possible_moves = find_all_possible_moves(board_fen)

    if maximizingPlayer:
        improved_possible_moves = prioritize_check(board_fen, possible_moves)
        maxEval = ac_global.INT_MIN
        best_move = None
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
