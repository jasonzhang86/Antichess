import chess
import numpy as np

Pawn_Value = 100
Knight_Value = 280
Bishop_Value = 320
Rook_Value = 479
Queen_Value = 929
King_Value = 60000
Chess_Value = [Pawn_Value, Knight_Value, Bishop_Value, Rook_Value, Queen_Value, King_Value]


Pawn_Square_Value = [0,   0,   0,   0,   0,   0,   0,   0,
            78,  83,  86,  73, 102,  82,  85,  90,
             7,  29,  21,  44,  40,  31,  44,   7,
           -17,  16,  -2,  15,  14,   0,  15, -13,
           -26,   3,  10,   9,   6,   1,   0, -23,
           -22,   9,   5, -11, -10,  -2,   3, -19,
           -31,   8,  -7, -37, -36, -14,   3, -31,
             0,   0,   0,   0,   0,   0,   0,   0]
        
Knight_Square_Value = [-66, -53, -75, -75, -10, -55, -58, -70,
            -3,  -6, 100, -36,   4,  62,  -4, -14,
            10,  67,   1,  74,  73,  27,  62,  -2,
            24,  24,  45,  37,  33,  41,  25,  17,
            -1,   5,  31,  21,  22,  35,   2,   0,
           -18,  10,  13,  22,  18,  15,  11, -14,
           -23, -15,   2,   0,   2,   0, -23, -20,
           -74, -23, -26, -24, -19, -35, -22, -69]

Bishop_Square_Value = [-59, -78, -82, -76, -23,-107, -37, -50,
           -11,  20,  35, -42, -39,  31,   2, -22,
            -9,  39, -32,  41,  52, -10,  28, -14,
            25,  17,  20,  34,  26,  25,  15,  10,
            13,  10,  17,  23,  17,  16,   0,   7,
            14,  25,  24,  15,   8,  25,  20,  15,
            19,  20,  11,   6,   7,   6,  20,  16,
            -7,   2, -15, -12, -14, -15, -10, -10]

        
Rook_Square_Value = [35,  29,  33,   4,  37,  33,  56,  50,
            55,  29,  56,  67,  55,  62,  34,  60,
            19,  35,  28,  33,  45,  27,  25,  15,
             0,   5,  16,  13,  18,  -4,  -9,  -6,
           -28, -35, -16, -21, -13, -29, -46, -30,
           -42, -28, -42, -25, -25, -35, -26, -46,
           -53, -38, -31, -26, -29, -43, -44, -53,
           -30, -24, -18,   5,  -2, -18, -31, -32]

Queen_Square_Value = [6,   1,  -8,-104,  69,  24,  88,  26,
            14,  32,  60, -10,  20,  76,  57,  24,
            -2,  43,  32,  60,  72,  63,  43,   2,
             1, -16,  22,  17,  25,  20, -13,  -6,
           -14, -15,  -2,  -5,  -1, -10, -20, -22,
           -30,  -6, -13, -11, -16, -11, -16, -27,
           -36, -18,   0, -19, -15, -15, -21, -38,
           -39, -30, -31, -13, -31, -36, -34, -42]

King_Square_Value = [4,  54,  47, -99, -99,  60,  83, -62,
           -32,  10,  55,  56,  56,  55,  10,   3,
           -62,  12, -57,  44, -67,  28,  37, -31,
           -55,  50,  11,  -4, -19,  13,   0, -49,
           -55, -43, -52, -28, -51, -47,  -8, -50,
           -47, -42, -43, -79, -64, -32, -29, -32,
            -4,   3, -14, -50, -57, -18,  13,   4,
            17,  30,  -3, -14,   6,  -1,  40,  18]

Pawn_Square_Matrix = np.array(Pawn_Square_Value).reshape((8, 8))
Knight_Square_Matrix = np.array(Knight_Square_Value).reshape((8, 8))
Bishop_Square_Matrix = np.array(Bishop_Square_Value).reshape((8, 8))
Rook_Square_Matrix = np.array(Rook_Square_Value).reshape((8, 8))
Queen_Square_Matrix = np.array(Queen_Square_Value).reshape((8, 8))
King_Square_Matrix = np.array(King_Square_Value).reshape((8, 8))



Square_Value = [Pawn_Square_Matrix, Knight_Square_Matrix, Bishop_Square_Matrix, Rook_Square_Matrix, Queen_Square_Matrix, King_Square_Matrix]

def evaluation_function(board_fen, desired_player):
    # Here the evaluation function is respect to White
    white_value = 0
    black_value = 0
    current_board = chess.Board(board_fen)
    for type in range (1, 7):
        white_position_list = current_board.pieces(type, True)
        black_position_list = current_board.pieces(type, False)
        for pos in white_position_list:
            white_value += Chess_Value[type-1]
            white_value += Square_Value[type-1][7-(pos//8)][pos % 8]
        for pos in black_position_list:
            black_value += Chess_Value[type-1]
            black_value += Square_Value[type-1][7-((63-pos)//8)][(63-pos) % 8]
    if desired_player == True: # If judged player is White
        return white_value - black_value
        
    else: # If judeged player is Black
        return black_value - white_value

