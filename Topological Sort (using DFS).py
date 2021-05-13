from collections import defaultdict


class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)

    def addEdge(self,u,v):
        #directed
        self.neighbours[u].append(v)
        self.finishedStack=[]

   
    def DFS(self,node,visited):
        visited[node]=True
        for v in self.neighbours[node]:
            if(not visited[v]):
                self.DFS(v,visited)

        self.finishedStack.append(node)


    def topoSort(self):
        print("This is the order of my courses—")
        while self.finishedStack:
            print(self.finishedStack.pop(),end=", ")
            

#assuming the graph is a DAG

g=Graph()
g.addEdge("Intro to Programming","Python")
g.addEdge("Intro to Programming","Java")
g.addEdge("Python","Adv. Python")
g.addEdge("Java","Adv. Java")
g.addEdge("Adv. Java","Thesis")
g.addEdge("Adv. Python","Thesis")

visited=defaultdict(lambda:False)

g.DFS("Intro to Programming",visited)
g.topoSort()
