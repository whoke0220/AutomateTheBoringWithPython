# TicTacToe game

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

win = False
winningPlayer = ''

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkForWin(board):
    #Top row winner
    if board['top-L'] == board['top-M'] and board['top-L'] == board['top-R']:
        win = True
        winningPlayer = board['top-L']

    #Left most column winner
    elif board['top-L'] == board['mid-L'] and board['top-L'] == board['low-L']:
        win = True
        winningPlayer = board['top-L']

    #Diagonal top-to-bottom, left-to-right winner
    elif board['top-L'] == board['mid-M'] and board['top-L'] == board['low-R']:
        win = True
        winningPlayer = board['top-L']

    #middle vertical winner
    elif board['top-M'] == board['mid-M'] and board['top-M'] == board['low-M']:
        win = True
        winningPlayer = board['top-M']

    #right most column winner
    elif board['top-R'] == board['mid-R'] and board['top-R'] == board['low-R']:
        win = True
        winningPlayer = board['top-R']

    #middle row winner
    elif board['mid-L'] == board['mid-M'] and board['mid-L'] == board['mid-R']:
        win = True
        winningPlayer = board['mid-L']

    #bottom row wimmer
    elif board['low-L'] == board['low-M'] and board['low-L'] == board['low-R']:
        win = True
        winningPlayer = board['low-L']

    #diagonal left to right, top to bottom winner
    elif board['low-L'] == board['mid-M'] and board['low-L'] == board['top-R']:
        win = True
        winningPlayer = board['low-L']

    else:
        win = False

turn = 'X'
numTurns = 0

while win != True or numTurns < 9:
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
    checkForWin(theBoard)

if win == True:
    print('The winner is: ' + winningPlayer)
else:
    print('No one wins!')
