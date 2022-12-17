import chess
import ac_global
from ac_exception import *

def get_opponent_color():
    if ac_global.my_player == chess.WHITE:
        return chess.BLACK
    elif ac_global.my_player == chess.BLACK:
        return chess.WHITE
    else:
        raise InvalidPlayerTypeException