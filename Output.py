class Output:

    def __init__(self, nodes, depth, solution):
        self.nodes = nodes
        self.depth = depth
        self.solution = solution

    def printOutput(self):
        print("Nodes Explored: ", self.nodes)
        print("Depth of the search: ", self.depth)
        print("Steps to solution: ")
        for board in self.solution:
            for i in range(0, 3):
                print(board[i])
            print("\n----------------------\n")
