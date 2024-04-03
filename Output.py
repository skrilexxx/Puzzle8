class Output:

    def __init__(self, nodes, depth):
        self.nodes = nodes
        self.depth = depth


    def printOutput(self):
        print("Nodes Explored: ", self.nodes)
        print("Depth of the search: ", self.depth)
        print("Path: ")