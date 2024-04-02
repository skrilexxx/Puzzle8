from Board import Board
from Solver import Solver




board = Board([[8, 1, 3,],[4, 0, 2],[7, 6, 5]])

print(board.isGoal())
print("Not in rigth place: ",board.hamming())
print("Distance: ", board.manhattan())
board.printBoard()
board.neighbors()
print("Is board 1 solvable ?: ", board.isSolvable())

#board2 = Board([[1, 2, 3],[4, 5, 6],[8, 7, 0]])
#print("Is board 2 solvable ?: ", board2.isSolvable())

test1 = Solver([[8, 1, 3],[4, 0, 2],[7, 6, 5]])
#test1.bruteForce([test1.board])
test1.solver()
