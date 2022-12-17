import chess
import ac_global
import valid_move

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

def make_a_move():
    if ac_global.board.turn == chess.WHITE:
        uci = input("White to move: ")
    else:
        uci = input("Black to move: ")
    move = chess.Move.from_uci(uci)
    if valid_move.antichess_is_legal(move):
        ac_global.board.push(move)
        print(ac_global.board)
    else:
        raise ValueError("Illegal move.")




    
    

if __name__ == "__main__":
    setup_game()
    print("Game start!")
    while not ac_global.board.is_game_over():
        try:
            make_a_move()
        except ValueError:
            print("Received an invalid move. Please enter again.")
            print(ac_global.board)
    print(ac_global.board.outcome())



