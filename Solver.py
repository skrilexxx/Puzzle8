from Board import *

class Solver:

    def __init__(self, input):
        self.input = input
        self.board = Board(input)
        self.solution = []
        self.moves = 0
        self.prevBoard = None

    def solver(self):
        if self.board.isGoal():
            self.solution.append(self.board.tiles)
            return self.solution
        else:
            self.solution.append(self.board.tiles)
            #print(self.solution)

            while not self.board.isGoal():
                self.board = self.next_move()
                self.solution.append(self.board.tiles)
                #print(self.solution)
                self.moves += 1
                self.prevBoard = self.solution[self.moves]
                self.showProgress()

            print("Number of moves: ", self.moves)

            return self.solution[-1]

    def next_move(self):
        neighbors = self.board.neighbors()
        hamming = []
        manhattan = []

        for neighbor in neighbors:
            hamming.append(neighbor.hamming())
            manhattan.append(neighbor.manhattan())

        if neighbors[hamming.index(min(hamming))].tiles != self.prevBoard:
            return neighbors[hamming.index(min(hamming))]
        else:
            return neighbors[hamming.index(min(hamming)+1)]




    def showProgress(self):
        for i in range(0, 3):
            print(self.solution[self.moves][i])
        print("Moves: ", self.moves)
        print("-----------------")



    def solution(self):
        return self.solution

test1 = Solver([[8, 1, 3],[4, 0, 2],[7, 6, 5]])
test1.solver()
