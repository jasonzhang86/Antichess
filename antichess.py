import chess
import argparse

import ac_global
from ac_exception import *
from ac_utils import *
from ac_search import *

"""
    Antichess program for CO 456 Final Project (Fall 2022)

    Python version: 3.9.13

    Prerequisite: python-chess, version 1.9.9 (can be installed using 'pip install chess')
    Library documentation: https://python-chess.readthedocs.io/en/latest/
    Github: https://github.com/niklasf/python-chess
""" 

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

def make_a_move():
    """
    Try to make a move using Minimax strategy and Alpha-Beta pruning.
    """  
    alpha = ac_global.INT_MIN
    beta = ac_global.INT_MAX

    # determine an optimal move with the two lists
    optimal_result = minimax_pruning(board_fen=ac_global.board.fen(), depth=4, alpha=alpha, beta=beta, maximizingPlayer=True)
    optimal_score = optimal_result[0]
    optimal_move = optimal_result[1]
    ac_global.board.push(optimal_move)
    print(optimal_move.uci())
    # For debugging
    print_message("My player [{}] moving to {}.".format(chess_color_to_string(ac_global.my_player), optimal_move.uci()))
    print_message("My move has score {}.".format(optimal_score))
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
