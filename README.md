# Antichess 
Final project for the Game Theory course in Fall 2022. Ruling is identical to standard chess, except with one additional rule:
  - If the player to move has a legal chess move which captures an opponent’s piece, then the player to move must make a legal chess move which captures an opponent’s piece.  
  
**Build instruction**:
  - Please clone the latest version from main branch. (The version for submission will be the latest version on the main branch.)
  - Python version: 3.9.13 (other version might also work)
  - To run the program: python/python3 .\antichess.py [white/black] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Assuming all the files are under the current directory)
  - The program expects one command line argument for determing its player's color.
  - When it's the program's turn, it will print one move in coordinate algebraic notation to STDOUT.  
    When it's the opponent's turn, it will read one move in coordinate algebraic notation from STDIN.
  - The program expects all moves from opponent to be valid, though it has some error handling (e.g. detecting invalid move).  
  
**Prerequisite and Reference**:
  - This program is based on the python chess library (python-chess). It can be installed using pip: "pip/pip3 install chess" (or "pip/pip3 install python-chess")  
    Library documentation: https://python-chess.readthedocs.io/en/latest/  
    Github: https://github.com/niklasf/python-chess  
  - The evaluation function used by this antichess program is based on the PeSTO's Evaluation Function.  
    Wiki Link: https://www.chessprogramming.org/PeSTO%27s_Evaluation_Function  
    
 **Other information**:
  - Before running the program, please make sure the "DEBUG" flag in the ac_global.py file is set to FALSE. (Otherwise it will print out the debug messages as well which will influence the match)  
  - When running the program, if error is encountered and is one of "NoLegalAntichessMoveException", "IllegalPlayerTypeException" and "IllegalMoveException", then it indicates detection of illegal behaviour. (though theoretically such behaviour will be detected by the software running the matches)
