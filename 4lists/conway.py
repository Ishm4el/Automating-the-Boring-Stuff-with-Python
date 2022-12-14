# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        # if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append(' ') # Add a dead cell
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop
    print('\n\n\n\n\n') # Seperate each step with newline
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the scree:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # print the # or space.
        print() # print a newline at the end of the row

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighboring coordinates:
            # '% width' ensure leftcoord is always between 0 and width - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # topleft neightbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # top neighbor is alive
            if currentCells[leftCoord][y] == '#':   
                numNeighbors += 1 # top neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # top neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # top neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # top neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # top neighbor is alive

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neightbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neightbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering



                
