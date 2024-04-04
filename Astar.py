from queue import PriorityQueue
from Board import Board
from Output import Output
import copy

class Astar:

    def __init__(self, start, goal, priFunction): #priorityFunc(True = Manhattan, False = Hamming)
        self.startBoard = start
        self.goalBoard = goal
        self.priorityFunction = priFunction


    def priority(self, board, depth): #priority function
        if self.priorityFunction:
            return depth + board.manhattan(self.goalBoard.tiles)
        else:
            return depth + board.hamming(self.goalBoard.tiles)


    def addPath(self, path, board):
        nPath = copy.deepcopy(path)
        nPath.append(board.tiles)
        return nPath


    def run(self):
        visited = []
        path = []
        nodesExplored = 1
        priorityQueue = PriorityQueue() #vytvoření queue
        priorityQueue.put((self.priority(self.startBoard, 0), 0, self.startBoard.tiles, path)) #přidání startovního stavu do queue (priority, depth, board)

        if self.startBoard.isSolvable() == False: #pokud není možné dosáhnout cíle
            return Output(None, None, None)

        while not priorityQueue.empty():
            priority, depth, board, path = priorityQueue.get()
            newBoard = Board(board)
            if newBoard.isGoal(self.goalBoard.tiles): #pokud je dosaženo cíle
                return Output(nodesExplored, depth, nPath) #vrátí výstup

            visited.append(board) #přidání boardu do navštívených

            for neighbor in newBoard.neighbors():
                if neighbor not in visited:
                    nodesExplored += 1
                    nDepth = depth + 1
                    nPath = self.addPath(path, neighbor)
                    priorityQueue.put((self.priority(neighbor, nDepth), nDepth, neighbor.tiles, nPath))

        return None