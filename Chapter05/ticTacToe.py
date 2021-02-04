# TicTacToe game

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

GameWin = False
winningPlayer = ''

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkForWin(board):
    print('Checking for winner.')
    global winningPlayer
    #Top row winner
    if board['top-L'] != ' ' and board['top-L'] == board['top-M'] and board['top-L'] == board['top-R']:
        winningPlayer = board['top-L']
        return True

    #Left most column winner
    elif board['top-L'] != ' ' and board['top-L'] == board['mid-L'] and board['top-L'] == board['low-L']:
        winningPlayer = board['top-L']
        return True

    #Diagonal top-to-bottom, left-to-right winner
    elif board['top-L'] != ' ' and board['top-L'] == board['mid-M'] and board['top-L'] == board['low-R']:
        winningPlayer = board['top-L']
        return True

    #middle vertical winner
    elif board['top-M'] != ' ' and board['top-M'] == board['mid-M'] and board['top-M'] == board['low-M']:
        winningPlayer = board['top-M']
        return True

    #right most column winner
    elif board['top-R'] != ' ' and board['top-R'] == board['mid-R'] and board['top-R'] == board['low-R']:
        winningPlayer = board['top-R']
        return True

    #middle row winner
    elif board['mid-L'] != ' ' and board['mid-L'] == board['mid-M'] and board['mid-L'] == board['mid-R']:
        winningPlayer = board['mid-L']
        return True

    #bottom row wimmer
    elif board['low-L'] != ' ' and board['low-L'] == board['low-M'] and board['low-L'] == board['low-R']:
        winningPlayer = board['top-L']
        return True

    #diagonal left to right, top to bottom winner
    elif board['low-L'] != ' ' and board['low-L'] == board['mid-M'] and board['low-L'] == board['top-R']:
        winningPlayer = board['top-L']
        return True

    else:
        return False

turn = 'X'
numTurns = 0

while GameWin != True:
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if theBoard[move] == ' ':
        theBoard[move] = turn
    else:
        print('Invalid move. Lose a turn')
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    numTurns += 1
    if numTurns >= 4:
        GameWin = checkForWin(theBoard)

if GameWin == True:
    print('The winner is: ' + winningPlayer)
    printBoard(theBoard)
else:
    print('No one wins!')
    printBoard(theBoard)
