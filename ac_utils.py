import chess
import ac_global

def print_board():
    if ac_global.DEBUG:
        print(ac_global.board.unicode(invert_color=True))

def print_game_result():
    if ac_global.DEBUG:
        print(ac_global.board.outcome())
        print(ac_global.board.result())

def print_message(message):
    if ac_global.DEBUG:
        print(message)

def chess_color_to_string(color):
    if color == chess.WHITE:
        return "WHITE"
    else:
        return "BLACK"