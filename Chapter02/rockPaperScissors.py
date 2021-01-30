#Rock, Paper, Scissors game

import random, sys

print('ROCK, PAPER, SCISSORS')

#These variables keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

while True: #main game loop
    print('% Wins, % Losses, % Ties'%(wins, losses, ties))
    while True: #Player input loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit the program
        if playerMove == 'r' or playerMove == 'p' 0r playerMove == 's':
            break #Break out of the input loop
        print('Type one of r, p, s or q')

    #Display player's choice
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    
