from Board import Board
from Astar import Astar
import os

class Input:

    def __init__(self, inputB) -> None:
        self.inputB = inputB
        self.goal = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]
        self.check = [1, 2, 3, 4, 5, 6, 7, 8, 0]


    def readInput(self):
        inputBoard = self.inputB

        print("Goal state is: ")
        for i in range(3):
            print(self.goal[i])

        if inputBoard is None:
            inputBoard = [[],[],[]]
            print("Enter the initial state of the board, one row at a time (example: 1 2 3):")
            for i in range(3):
                inputBoard[i] = list(map(int, input().split()))

            if not self.isValid(inputBoard):
                print("Invalid input")
                return None
            else:
                print("Initial state is: ")
                for i in range(3):
                    print(inputBoard[i])

                return Board(inputBoard)
        else:
            print("Initial state is: ")
            for i in range(3):
                print(inputBoard[i])

            return Board(inputBoard)

    def isValid(self, inputBoard):
        if len(inputBoard) != 3:
            return False

        for i in range(3):
            if len(inputBoard[i]) != 3:
                return False


        for i in range(3):
            for j in range(3):
                if inputBoard[i][j] not in self.check:
                    print(inputBoard[i][j])
                    return False
                else:
                    self.check.remove(inputBoard[i][j])



        return True

    def run(self):
        board = self.readInput()
        if board is None:
            return None

        star = Astar(board, Board(self.goal), True)

        result = star.run()

        if result is None:
            print("No solution")
        else:
            result.printOutput()
