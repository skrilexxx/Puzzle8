class Output:

    def __init__(self, nodes, depth, path):
        self.nodes = nodes
        self.depth = depth
        self.path = path


    def printOutput(self):
        if self.path is None:
            print("No solution, can't be solved.")
            return
        else:
            print("Path: ")
            for i in range(0, len(self.path)):
                print("Step: ", i+1)
                for item in self.path[i]:
                    print(item)
                print("-----------")

            print("")
            print("Solution found")
            print("Nodes Explored: ", self.nodes)
            print("Depth of the search: ", self.depth)