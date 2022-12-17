import chess
import ac_global

def antichess_legal_moves():
    chess_move_list = ac_global.board.pseudo_legal_moves
    antichess_move_list = []
    for move in chess_move_list:
        if ac_global.board.is_capture(move) == True:
            antichess_move_list.append(move)
    if not antichess_move_list:
        antichess_move_list = chess_move_list
    print(antichess_move_list)
    return antichess_move_list

def antichess_is_legal(move):
    if move in antichess_legal_moves():
        return True
    else:
        return False