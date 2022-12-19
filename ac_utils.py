import chess
import ac_global
from ac_exception import *

def get_opponent_color():
    if ac_global.my_player == chess.WHITE:
        return chess.BLACK
    elif ac_global.my_player == chess.BLACK:
        return chess.WHITE
    else:
        raise InvalidPlayerTypeException("Player must be one of white and black.")

def input_by_color(message):
    if ac_global.board.turn == chess.WHITE:
        res = input("White " + message)
    else:
        res = input("Black " + message)
    return res
    
def print_by_color(message):
    if ac_global.board.turn == chess.WHITE:
        print("White " + message)
    else:
        print("Black " + message)
