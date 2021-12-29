def isValidChessBoard(chessBoard):
    # Variables for max number of pieces a player can have and the max number of
    # pawns each player can have.
    max_number_of_pieces = 16
    max_number_of_pawns = 8
    valid_row_numbers = '12345678'
    valid_column_letters = 'abcdefgh'
    
    #counters for each player's pieces. Initialized at 0
    white_pieces = 0
    black_pieces = 0
    black_king = 0
    white_king = 0
    black_pawns = 0
    white_pawns = 0
    
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
    
    if black_pieces > max_number_of_pieces or white_pieces > max_number_of_pieces:
        print('Too many pieces on the board for a player making this board invalid')
        return False
    
    # Check for a maximum of 8 pawns
    for piece in chessBoard.values():
        if piece == 'bpawn':
            black_pawns += 1
        if piece == 'wpawn':
            white_pawns += 1
            
    if black_pawns > max_number_of_pawns or white_pawns > max_number_of_pawns:
        print('One of the players has too many pawns making this board invalid.')
        return False
    
    #check for valid space naming
    for space in chessBoard.keys():
        if space[0] not in valid_row_numbers:
            print('Invalid row listed making this board invalid.')
            return False
        if space[1] not in valid_column_letters:
            print('Invlaid column listed making this board invalid.')
            return False
    
    return True


test_board_1 = {'1h':'bking', '6c':'wqueen', '2g':'bbishop',
             '5h':'bqueen', '3e':'wking'}

test_board_2 = {"1a": "bpawn", "2a": "wking"}

test_board_3 = {"1a": "wking", "2a": "wking", "3c": "bbishop"}

test_board_4 = {"1a": "bking", "9z": "wking"}

if (isValidChessBoard(test_board_1)):
    print('Valid board.')
    
if (isValidChessBoard(test_board_2)):
    print('Valid board.')
    
if (isValidChessBoard(test_board_3)):
    print('Valid board.')
    
if (isValidChessBoard(test_board_4)):
    print('Valid board.')