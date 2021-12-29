# Variables for max number of pieces a player can have and the max number of
# pawns each player can have.
max_number_of_pieces = 16
max_number_of_pawns = 8

def isValidChessBoard(chessBoard):
    #value to return determining if board is valid or not
<<<<<<< HEAD
    # Defaults to return an invalid board.
    isValidBoard = False
    white_pieces_valid = False
    black_pieces_valid = False
    
    

    return isValidBoard



the_board = {'1h':'bking', '6c':'wqueen', '2g':'bbishop',
             '5h':'bqueen', '3e':'wking'}

if isValidChessBoard(the_board):
    print('The board is valid.')
=======
    isValidBoard = False
    white_pieces_valid = False
    black_pieces_valid = False

    #Set initial counter variables to 0. Will be used to track the number of
    #pieces in each subset.
    number_of_black_kings = 0
    number_of_white_kings = 0
    number_of_black_pawns = 0
    number_of_white_pawns = 0
    number_of_black_pieces = 0
    number_of_white_pieces = 0

    for piece in chessBoard.values():
        #Process black pieces
        if(piece[0] == "b"):
            number_of_black_pieces += 1
            #Determine piece type and number of pieces

            #Determine if pawn
            if(piece[1] == "p"):
                number_of_black_pawns += 1
                number_of_black_pieces += 1

            #determine if king
            elif(piece[1] == "k"):
                number_of_black_kings += 1
                number_of_black_pieces += 1

            #count all other pieces
            else:
                number_of_black_pieces += 1

        elif(piece[0] == "w"):
            number_of_white_pieces += 1
        else
            isValidBoard = False

    return isValidBoard
>>>>>>> 9c505e096c6e09ed4f73f68da5b3fc86ba66c3bf
