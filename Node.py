from Board import Board

class Node:
    def __init__(self, data):
        self.initial = data
        self.prevouris = None
        self.moves = 0