
#Welcome to ThatProfGuy! 

import sys
import math
from collections import defaultdict,deque
try: 
    sys.stdin = open('input.txt', 'r') 
    sys.stdout = open('output.txt', 'w')
 
except: 
    pass
 


class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)

    def addEdge(self,u,v,bidirec=True):
        self.neighbours[u].append(v)
        if(bidirec):
            self.neighbours[v].append(u)


    def BFS(self,source):
        visited=defaultdict(lambda:False)
        distance=defaultdict(lambda:float("inf"))
        distance[source]=0
        visited[source]=True
        queue=deque([source])
        parent={}
        parent[source]=None
        while queue:
            u=queue.popleft()
            print(u,end="->")
            for v in self.neighbours[u]:
                if(not visited[v]):
                    visited[v]=True
                    queue.append(v)
                    distance[v]=distance[u]+1
                    parent[v]=u


        print()
        print(distance)
        print(parent)


g=Graph()
number_of_edges=5
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(4,6)

g.BFS(1)


