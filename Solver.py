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
        average =  []

        for neighbor in neighbors:
            if neighbor.tiles != self.prevBoard:
                hamming.append(neighbor.hamming())
                manhattan.append(neighbor.manhattan())
            else:
                neighbors.remove(neighbor)


        for i in range(0, len(hamming)):
            average.append((hamming[i] + manhattan[i])/2)


        #print("Hamming: ", hamming)
        #print("Manhattan: ", manhattan)
        #print("Average: ", average)


        if neighbors[average.index(min(average))].tiles == self.solution[self.moves-1]:
            for number in average:
                if number > min(average) and number < max(average):
                    return neighbors[average.index(number)]

            return neighbors[average.index(max(average))]
        else:
            return neighbors[average.index(min(average))]



    def bruteForce(self, listOfObject):
        inputList = listOfObject
        output = []

        for i in range(0, len(inputList)):
            if inputList[i].isGoal():
                return inputList[i]
            else:
                for neighbor in inputList[i].neighbors():
                    output.append(neighbor)

        return self.bruteForce(output)





    def showProgress(self):
        for i in range(0, 3):
            print(self.solution[self.moves][i])
        print("Moves: ", self.moves)
        print("-----------------")



    def solution(self):
        return self.solution
