import chess
import random
import ac_global
from ac_exception import *
from ac_utils import *

def determine_player(player):
    if player == "white":
        print("You are the white player.")
        return chess.WHITE
    elif player == "black":
        print("You are the black player.")
        return chess.BLACK
    else:
        raise InvalidPlayerTypeException("Invalid player type [{}]. Please choose one of white and black.".format(player))

def setup_game():
    player = input("Choose your player: ")
    ac_global.my_player = determine_player(player)
    print("Initializing board.")
    ac_global.board = chess.Board()
    print(ac_global.board)

def receive_a_move():
    try:
        uci = input_by_color("to move: ")
        move = chess.Move.from_uci(uci)
        if ac_global.board.is_legal(move):
            print_by_color("moving to {}.".format(uci))
            ac_global.board.push(move)
            print(ac_global.board)
    except ValueError:
        raise InvalidMoveException("Received an illegal move. Please enter again.")

def is_valid_antichess_move(move):
    to_square_color = ac_global.board.color_at(move.to_square)
    return to_square_color == get_opponent_color()

def find_optimal_move(antichess_moves, possible_moves):
    if antichess_moves:
        return random.choice(antichess_moves)
    elif possible_moves:
        return random.choice(possible_moves)
    else:
        raise NoLegalAntichessMoveException("Cannot make a valid antichess move.")

def make_a_move():
    print_by_color("making a move.")

    # split all possible moves into regular/antichess moves
    possible_moves = list(ac_global.board.legal_moves)
    antichess_moves = []
    for move in possible_moves:
        if is_valid_antichess_move(move):
            possible_moves.remove(move)
            antichess_moves.append(move)

    # determine a move with the two lists
    optimal_move = find_optimal_move(antichess_moves, possible_moves)
    print_by_color("moving to {}.".format(optimal_move.uci()))
    ac_global.board.push(optimal_move)
    print(ac_global.board)

if __name__ == "__main__":
    setup_game()
    print("Game start!")
    while not ac_global.board.is_game_over():
        if ac_global.board.turn == ac_global.my_player:
            try:
                make_a_move()
            except NoLegalAntichessMoveException as e:
                print(e)
                break # Need to investigate what happens in this case.
        else:
            try:
                receive_a_move()
            except InvalidMoveException as e:
                print(e)
                print(ac_global.board)
    print(ac_global.board.outcome())
