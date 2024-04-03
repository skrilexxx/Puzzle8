from Board import Board
from Astar import Astar


board = Board([[8, 1, 3,],[4, 0, 2],[7, 6, 5]])
board2 = Board([[1, 2, 3],[4, 5, 6],[8, 7, 0]])
goal = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]
goalBoard = Board(goal)

star = Astar(board, goalBoard, True)

result = star.run()

if result is None:
    print("No solution")
else:
    result.printOutput()



"""
print(board.isGoal(goal))
print("Not in rigth place: ",board.hamming(goal))
print("Distance: ", board.manhattan(goal))
print("Empty tile at: ", board.getEmpty())
board.printBoard()
board.neighbors()
print("Is board 1 solvable ?: ", board.isSolvable())

print("Is board 2 solvable ?: ", board2.isSolvable())
"""