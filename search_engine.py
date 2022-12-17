import evaluation
import chess
import valid_move
INT_MAX = 100000000
INT_MIN = -100000000

def pruning_minimax(board_fen, depth, alpha, beta, current_player, desired_player):
    if depth == 0:
        return [evaluation.evaluation_function(board_fen, desired_player), '']
    current_board = chess.Board(board_fen)
    if current_board.is_game_over():
        return evaluation.evaluation_function(board_fen, desired_player)
    
    if current_player == desired_player:
        maxEval = INT_MIN
        for move in valid_move.antichess_legal_moves(current_board):
            current_board.push(move)
            new_fen = current_board.fen()
            current_board.pop()
            eval = pruning_minimax(new_fen, depth-1, alpha, beta, not current_player, desired_player)[0]
            if (alpha < eval):
                maxEval = max(alpha, eval)
                max_move = move.uci()
            if beta <= alpha:
                break
        return [maxEval, max_move]

    else:
        minEval = INT_MAX
        for move in valid_move.antichess_legal_moves(current_board):
            current_board.push(move)
            new_fen = current_board.fen()
            current_board.pop()
            eval = pruning_minimax(new_fen, depth-1, alpha, beta, not current_player, desired_player)[0]
            minEval = min(beta, eval)
            if beta <= alpha:
                break
        return [minEval, '']
    