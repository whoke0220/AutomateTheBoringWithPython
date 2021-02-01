# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of lists for the cells:
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #Adds a living cell.
        else:
            column.append(' ') #Adds a dead cells
    nextCells.append(column) #a list of column lists

while True: #Main loop
    print('\n\n\n\n\n') #Clear seperation between steps
    currentCells = copy.deepcopy(nextCells)

    #Print currentCells to the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end='')
        print()

    #Calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        print('Current x: ' + str(x))
        for y in range(HEIGHT):
            print('Current y: ' + str(y))
            #Get neighboring coordinates:
            #`% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            #Count the number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][rightCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1

            #Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                #Everything else dies or stays dead:
                nextCells[x][y] = ' '
time.sleep(1)
