from Board import *

class Solver:

    def __init__(self, input):
        self.input = input
        self.board = Board(input)
        self.solution = []

    def solver(self):
        pass

    def moves(self):
        pass

    def solution(self):
        return self.solution


test1 = Solver([[8, 1, 3],[4, 0, 2],[7, 6, 5]])
print(test1.solver())
