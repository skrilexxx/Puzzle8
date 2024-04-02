class Board:
    def __init__(self, tiles):
        self.tiles = tiles
        self.size = 9;

    def printBoard(self):
        for list in self.tiles:
            print(list)

    def tileAt(self, i, j):
        return self.tiles[i][j]


    def size(self):
        return self.size

    def copyBoard(self, copyBoard):
        for i in range(0, 3):
            for y in range(0, 3):
                copyBoard[i].append(self.tiles[i][y])
        return copyBoard

    # number of tiles out of place
    def hamming(self, goalBoard):
        notInPlace = 0
        for i in range (0, 3):
            for y in range (0, 3):
                if self.tiles[i][y] != goalBoard[i][y]:
                    if self.tiles[i][y] != 0:
                        notInPlace += 1
        return notInPlace

    # sum of Manhattan is a sum of distances between each tile and goal position
    def manhattan(self, goalBoard):
        distance = 0
        position = []
        for i in range (0, 3):
            for y in range (0, 3):
                if goalBoard[i][y] != self.tiles[i][y] and goalBoard[i][y] != 0:
                    #moves = 0
                    for list in self.tiles:
                        if goalBoard[i][y] in list:
                            position.append(self.tiles.index(list))
                            position.append(list.index(goalBoard[i][y]))
                    distance += abs((position[0] - i))
                    distance += abs((position[1] - y))
                    """
                    debug
                    moves += abs((position[0] - i))
                    moves += abs((position[1] - y))
                    print("From: ", position, " To: [", i, ",", y, "]")
                    print("Moves for this tile:", moves)
                    print("Distance: ", distance)
                    """
                    position.clear()
        return distance



    # is this board the goal board? - jde to napsat na 1 line mozna
    def isGoal(self, goalBoard):
        if self.tiles == goalBoard:
            return True
        else:
            return False


    # return the position of the empty tile
    def getEmpty(self):
        for i in range(0, 3):
            for y in range(0, 3):
                if self.tiles[i][y] == 0:
                    return [i, y]

    def neighbors(self):
        listOfNeighbors = []
        positionOfZero = self.getEmpty()
        posiblePositions = []




        if positionOfZero == [1, 1]:
            posiblePositions = [[0, 1],[1, 0],[1, 2],[2, 1]]

        elif positionOfZero in [[0,0],[0, 2],[2, 0],[2, 2]]:
            if positionOfZero == [0, 0] or positionOfZero == [0, 2]:
                posiblePositions.append([0, 1])
                posiblePositions.append([positionOfZero[0]+1, positionOfZero[1]])
            else:
                posiblePositions.append([2, 1])
                posiblePositions.append([positionOfZero[0]-1, positionOfZero[1]])

        else:
            if positionOfZero == [0, 1] or positionOfZero == [2, 1]:
                posiblePositions.append([positionOfZero[0], 0])
                posiblePositions.append([positionOfZero[0], 2])
                posiblePositions.append([1, 1])
            else:
                posiblePositions.append([0, positionOfZero[1]])
                posiblePositions.append([2, positionOfZero[1]])
                posiblePositions.append([1, 1])

        #print("Posible positions: ", posiblePositions)
        for position in posiblePositions:
            #print("Position: ", position)
            neighbor = [[],[],[]]
            neighbor = self.copyBoard(neighbor) #nefunguje mi .copy(), pořád se to propisovalo
            number = neighbor[position[0]][position[1]]
            neighbor[position[0]][position[1]] = 0
            neighbor[positionOfZero[0]][positionOfZero[1]] = number
            listOfNeighbors.append(Board(neighbor))

        """
        for i in range(len(listOfNeighbors)):
            print("Move: ", i+1)
            listOfNeighbors[i].printBoard()
            print("----------")
        """
        positionOfZero.clear()
        return listOfNeighbors

    def isSolvable(self):
        inversions = 0
        allTiles = []

        for row in self.tiles:
            for number in row:
                allTiles.append(number)

        for j in allTiles:
            for i in range(0, len(allTiles)):
                if allTiles[i] < j and i > allTiles.index(j) and allTiles[i] != 0 and j != 0:
                    #print("Number one:", allTiles[i], " Position:", i )
                    #print("Number two", j, " Position: ", allTiles.index(j))
                    inversions += 1

        #print(inversions)
        #print(allTiles)

        if inversions%2 == 0:
            return True
        else:
            return False
