class NoLegalAntichessMoveException(Exception):
    "Cannot make a valid antichess move"
    pass

class InvalidPlayerTypeException(Exception):
    "Invalid Player Type. Player must be one of white and black."
    pass