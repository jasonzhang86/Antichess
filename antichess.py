import chess
import ac_global
import search_engine

def determine_player(player: str):
    if player == "white":
        print("AI is the white player.")
        return chess.WHITE
    elif player == "black":
        print("AI is the black player.")
        return chess.BLACK
    else:
        raise TypeError("Invalid player type [{}]. Please choose one of white and black.".format(player))

def setup_game():
    player = input("Choose AI player: ")
    ac_global.AI_player = determine_player(player)
    print("Initializing board.")
    ac_global.board = chess.Board()
    print(ac_global.board)

def make_a_move():
    alpha = ac_global.INT_MIN
    beta = ac_global.INT_MAX
    if ac_global.AI_player == chess.WHITE:
        AI_move_uci = search_engine.pruning_minimax(ac_global.board.fen(), 3, alpha, beta, True, True)[1]
        AI_move = chess.Move.from_uci(AI_move_uci)
        print("AI choose to move:", AI_move_uci)
        ac_global.board.push(AI_move)
        print(ac_global.board)
        player_uci = input("Black to move: ")
        player_move = chess.Move.from_uci(player_uci)
        ac_global.board.push(player_move)
        print(ac_global.board)
    else:
        player_uci = input("White to move: ")
        player_move = chess.Move.from_uci(player_uci)
        ac_global.board.push(player_move)
        print(ac_global.board)
        AI_move_uci = search_engine.pruning_minimax(ac_global.board.fen(), 3, alpha, beta, False, False)[1]
        AI_move = chess.Move.from_uci(AI_move_uci)
        print("AI choose to move:", AI_move_uci)
        ac_global.board.push(AI_move)
        print(ac_global.board)

        
    


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



