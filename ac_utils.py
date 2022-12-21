import chess
import ac_global

def print_board():
    if ac_global.DEBUG:
        print(ac_global.board.unicode(invert_color=True))

def print_message(message):
    if ac_global.DEBUG:
        print(message)

def chess_color_to_string(color):
    if color == chess.WHITE:
        return "WHITE"
    elif color == chess.BLACK:
        return "BLACK"
    else:
        return "NONE"

def print_game_result():
    if ac_global.DEBUG:
        print(ac_global.board.outcome().termination)
        print_message(chess_color_to_string(ac_global.board.outcome().winner) + " wins!")