def isValidChessBoard(chessBoard):
    # Variables for max number of pieces a player can have and the max number of
    # pawns each player can have.
    max_number_of_pieces = 16
    max_number_of_pawns = 8
    
    #counters for each player's pieces. Initialized at 0
    white_pieces = 0
    black_pieces = 0
    black_king = 0
    white_king = 0
    
    #Check for a black and a white king
    if "bking" not in chessBoard.values() or "wking" not in chessBoard.values():
        print('Either a white king or a black king is not on the board making this board invalid.')
        return False
    
    #Check for exactly one black king and one white king
    for piece in chessBoard.values():
        if piece == 'bking':
            black_king += 1
        if piece == 'wking':
            white_king += 1
    if black_king != 1 or white_king != 1:
        print('Either player does not have exactly one king making this board invalid.')
        return False
    
    #Check for a maximum of 16 pieces for each player
    for piece in chessBoard.values():
        if piece[0] == 'b':
            black_pieces += 1
        elif piece[0] == 'w':
            white_pieces += 1
    
    if black_pieces >= 17 or white_pieces >= 17:
        print('Too many pieces on the board for a player making this board invalid')
        return False
    
    
    return True


the_board = {'1h':'bking', '6c':'wqueen', '2g':'bbishop',
             '5h':'bqueen', '3e':'wking'}

if (isValidChessBoard(the_board)):
    print('Valid board.')