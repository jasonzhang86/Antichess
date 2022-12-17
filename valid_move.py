import chess

def antichess_legal_moves(board):
    chess_move_list = board.pseudo_legal_moves
    antichess_move_list = []
    for move in chess_move_list:
        if board.is_capture(move) == True:
            antichess_move_list.append(move)
    if not antichess_move_list:
        antichess_move_list = chess_move_list
    return antichess_move_list

def antichess_is_legal(board, move):
    if move in antichess_legal_moves(board):
        return True
    else:
        return False