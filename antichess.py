import chess
import random
import ac_global
from ac_exception import *
from ac_utils import *

def determine_player(player: str):
    if player == "white":
        print("You are the white player.")
        return chess.WHITE
    elif player == "black":
        print("You are the black player.")
        return chess.BLACK
    else:
        raise TypeError("Invalid player type [{}]. Please choose one of white and black.".format(player))

def setup_game():
    player = input("Choose your player: ")
    ac_global.my_player = determine_player(player)
    print("Initializing board.")
    ac_global.board = chess.Board()
    print(ac_global.board)

def receive_a_move():
    if ac_global.board.turn == chess.WHITE:
        uci = input("White to move: ")
    else:
        uci = input("Black to move: ")
    move = chess.Move.from_uci(uci)
    if ac_global.board.is_legal(move):
        ac_global.board.push(move)
        print(ac_global.board)
    else:
        raise ValueError("Illegal move.")

def is_valid_antichess_move(move: chess.Move):
    to_square_color = ac_global.board.color_at(move.to_square)
    return to_square_color == get_opponent_color()

def find_optimal_move(antichess_moves: list[chess.Move], possible_moves: list[chess.Move]):
    if antichess_moves:
        return random.choice(antichess_moves)
    elif possible_moves:
        return random.choice(possible_moves)
    else:
        return NoLegalAntichessMoveException

def make_a_move():
    if ac_global.board.turn == chess.WHITE:
        print("White making a move.")
    else:
        print("Black making a move.")

    # split all possible moves into regular/antichess moves
    possible_moves = list(ac_global.board.legal_moves)
    antichess_moves = []
    for move in possible_moves:
        if is_valid_antichess_move(move):
            possible_moves.remove(move)
            antichess_moves.append(move)

    # determine a move with the two lists
    optimal_move = find_optimal_move(antichess_moves, possible_moves)
    ac_global.board.push(optimal_move)
    print(ac_global.board)

if __name__ == "__main__":
    setup_game()
    print("Game start!")
    while not ac_global.board.is_game_over():
        if ac_global.board.turn == ac_global.my_player:
            try:
                make_a_move()
            except NoLegalAntichessMoveException:
                print("Cannot make a valid antichess move.")
                break # Need to investigate what happens in this case.
        else:
            try:
                receive_a_move()
            except ValueError:
                print("Received an invalid move. Please enter again.")
                print(ac_global.board)
    print(ac_global.board.outcome())
