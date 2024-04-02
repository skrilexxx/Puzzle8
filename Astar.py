from queue import PriorityQueue
from Board import Board

def Astar(initial_state):
    count=0
    explored=[]
    start_node=Board(initial_state,None,None,0,True)
    q = PriorityQueue()
    q.put((start_node.evaluation_function,count,start_node))
