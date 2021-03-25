
from collections import defaultdict


class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)

    def addEdge(self,u,v,bidirec=True):
        self.neighbours[u].append(v)
        if(bidirec):
            self.neighbours[v].append(u)


    def DFS(self):
      print("Iterative DFS: ")
      stack=[1]
      visited=defaultdict(lambda:False)
      while stack:
        u=stack.pop()
        print("Visiting...",u)
        if(not visited[u]):
          visited[u]=True
          for v in self.neighbours[u]:
            if(not visited[v]):
              stack.append(v)

    def DFS_Recurse(self,node,visited):
      if(visited[node]):
        return
      print("Visiting ...",node)
      visited[node]=True
      for v in self.neighbours[node]:
        self.DFS_Recurse(v,visited)




  

g=Graph()
g.addEdge(1,6)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(4,7)
g.addEdge(7,8)
g.addEdge(8,9)
g.DFS()

print("Recursive DFS:")
visited=defaultdict(lambda:False)
g.DFS_Recurse(1,visited)
