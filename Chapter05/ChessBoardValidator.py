# Variables for max number of pieces a player can have and the max number of
# pawns each player can have.
max_number_of_pieces = 16
max_number_of_pawns = 8

def isValidChessBoard(chessBoard):
    #Set initial counter variables to 0. Will be used to track the number of
    #pieces in each subset.
    number_of_black_kings = 0
    number_of_white_kings = 0
    number_of_black_pawns = 0
    number_of_white_pawns = 0
    number_of_black_pieces = 0
    number_of_white_pieces = 0

    for piece in chessBoard.values():
