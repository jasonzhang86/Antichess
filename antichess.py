import chess
import random
import argparse

import ac_global
from ac_exception import *
from ac_utils import *

def setup_game():
    """
    Setup an antichess game.

    Parse one command line argument [player] and initialize the board
    """  
    
    # Parse command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('player', type=str)
    args = parser.parse_args()

    if args.player == "white":
        ac_global.my_player = chess.WHITE
        ac_global.opponent = chess.BLACK
    elif args.player == "black":
        ac_global.my_player = chess.BLACK
        ac_global.opponent = chess.WHITE
    else:
        raise IllegalPlayerTypeException("Illegal player type [{}]. Please choose one of white and black.".format(args.player))
    ac_global.board = chess.Board()
    print_board()

def receive_a_move():
    """
    Receive one move from opponent.

    If receives an illegal move, reject it and expect a new move from input (until a legal move is given).
    """  
    try:
        uci = input("Waiting for opponent to enter a move: ")
        move = chess.Move.from_uci(uci)
        if ac_global.board.is_legal(move):
            print_message("Opponent [{}] moving to {}.".format(chess_color_to_string(ac_global.opponent), uci))
            ac_global.board.push(move)
            print_board()
    except ValueError:
        raise IllegalMoveException("Received an illegal move. Please enter again.")

def is_antichess_move(move):
    return ac_global.board.is_capture(move)

def find_optimal_move(antichess_moves, regular_moves):
    if antichess_moves:
        return random.choice(antichess_moves)
    elif regular_moves:
        return random.choice(regular_moves)
    else:
        raise NoLegalAntichessMoveException("Cannot make a valid antichess move.")

def make_a_move():
    """
    Try to make a move using Minimax strategy and Alpha-Beta pruning.
    """  

    # split all possible moves into antichess/regular moves
    # :antichess move: moves that capture an opponent's piece, if such a move exists, we must make this move.
    # :regular move: moves that do not caputure an opponent's piece, we only consider such move if 
    #                there is no antichess move
    possible_moves = list(ac_global.board.legal_moves)
    antichess_moves = []
    regular_moves = []
    for move in possible_moves:
        if is_antichess_move(move):
            antichess_moves.append(move)
        else:
            regular_moves.append(move)

    # determine an optimal move with the two lists
    optimal_move = find_optimal_move(antichess_moves, regular_moves)
    print(optimal_move.uci())
    ac_global.board.push(optimal_move)

    # For debugging
    print_message("My player [{}] moving to {}.".format(chess_color_to_string(ac_global.my_player), optimal_move.uci()))
    print_board()

if __name__ == "__main__":
    setup_game()
    while not ac_global.board.is_game_over():
        if ac_global.board.turn == ac_global.my_player:
            try:
                make_a_move()
            except NoLegalAntichessMoveException as e:
                print(e)
                break 
        else:
            try:
                receive_a_move()

                # Game should switch turn after opponent makes a move
                if ac_global.board.turn == ac_global.opponent:
                    raise IllegalMoveException("Received an illegal move. Please enter again.")
            except IllegalMoveException as e:
                print(e)
                print_board()
    print_game_result()
    