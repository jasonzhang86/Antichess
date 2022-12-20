import evaluation
import chess
import valid_move
import ac_global
import random

# This is a function meant to order the choices we try at the same level of the game tree
def order_moves(board, move_list):
    check_move_list = []
    remaining_list = []
    for move in move_list:
        if board.gives_check(move) == True:
            check_move_list.append(move)
        else:
            remaining_list.append(move)
    random.shuffle(check_move_list)
    random.shuffle(remaining_list)
    return check_move_list + remaining_list


def pruning_minimax(board_fen, depth, alpha, beta, current_player, desired_player):
    if depth == 0:
        return [evaluation.evaluation_function(board_fen, desired_player), '']
    current_board = chess.Board(board_fen)
    if current_board.is_game_over():
        return [evaluation.evaluation_function(board_fen, desired_player), '']
    
    if current_player == desired_player:
        maxEval = ac_global.INT_MIN
        available_move_list = valid_move.antichess_legal_moves(current_board)
        improved_move_list = order_moves (current_board, available_move_list)
        for move in improved_move_list:
            current_board.push(move)
            new_fen = current_board.fen()
            current_board.pop()
            eval = pruning_minimax(new_fen, depth-1, alpha, beta, not current_player, desired_player)[0]
            if eval >= maxEval:
                maxEval = eval
                max_move = move.uci() 
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
        return [maxEval, max_move]

    else:
        minEval = ac_global.INT_MAX
        for move in valid_move.antichess_legal_moves(current_board):
            current_board.push(move)
            new_fen = current_board.fen()
            current_board.pop()
            eval = pruning_minimax(new_fen, depth-1, alpha, beta, not current_player, desired_player)[0]
            minEval = min(minEval, eval)
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return [minEval, '']
    