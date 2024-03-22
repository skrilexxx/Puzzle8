class Board:
    def __init__(self, tiles):
        self.tiles = tiles
        self.size = 0;
        self.goal = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]


    def print_board(self):
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
    def hamming(self):
        notInPlace = 0
        for i in range (0, 3):
            for y in range (0, 3):
                if self.tiles[i][y] != self.goal[i][y]:
                    if self.tiles[i][y] != 0:
                        notInPlace += 1
        return notInPlace
    
    # sum of Manhattan is a sum of distances between each tile and goal position
    def manhattan(self):
        distance = 0
        position = []
        for i in range (0, 3):
            for y in range (0, 3):
                if self.goal[i][y] != self.tiles[i][y] and self.goal[i][y] != 0:
                    #moves = 0
                    for list in self.tiles:
                        if self.goal[i][y] in list:
                            position.append(self.tiles.index(list))
                            position.append(list.index(self.goal[i][y]))
                    distance += abs((position[0] - i))
                    distance += abs((position[1] - y)) 
                    #debug
                    #moves += abs((position[0] - i))
                    #moves += abs((position[1] - y))
                    #print("From: ", position, " To: [", i, ",", y, "]")
                    #print("Moves for this tile:", moves)
                    #print("Distance: ", distance)
                    position.clear()
        return distance



    # is this board the goal board? - jde to napsat na 1 line mozna
    def isGoal(self):
        if self.tiles == self.goal:
            return True
        else:
            return False

    def neighbors(self):
        #listOfNeighbors = []
        positionOfZero = []

        for i in range(0, 3):
            for y in range(0, 3):
                if self.tiles[i][y] == 0:
                    positionOfZero.append(i)
                    positionOfZero.append(y)
                    break
        
        if positionOfZero == [1, 1]:
            return 4;
        elif positionOfZero in [[0,0],[0, 2],[2, 0],[2, 2]]:
            return 2;
        else:
            return 3;
        
        """
        if positionOfZero == [1, 1]:
            posiblePositions = [[0, 1],[1, 0],[1, 2],[2, 1]]

        toto ma byt az v solveru gg tady tak funkce ma vracet pouze 2, 3, 4 - to kolik muze mit negthbors
            for position in posiblePositions:
                neighbor = [[],[],[]]
                neighbor = self.copyBoard(neighbor) #nefunguje mi .copy(), pořád se to propisovalo
                number = neighbor[position[0]][position[1]]
                print(number)
                neighbor[position[0]][position[1]] = 0
                neighbor[1][1] = number
                print(neighbor)
                print("Tiles:", self.tiles)
                listOfNeighbors.append(neighbor)
        """
        print(positionOfZero)
        #print(listOfNeighbors)

    def isSolvable(self):
        pass



    
board = Board([[8, 1, 3,],[4, 0, 2],[7, 6, 5]])
copy = [[],[],[]]

print(board.isGoal())
print("Not in rigth place: ",board.hamming())
print("Distance: ", board.manhattan())
board.print_board()
print("Neighbors: ", board.neighbors())
