from collections import defaultdict


class Graph:
    def __init__(self,n):
        self.num_vertices=n
        self.neighbours=defaultdict(list)
        self.indegree=defaultdict(lambda:0)
        
      


    def addEdge(self,u,v):
        #directed
        self.neighbours[u].append(v)
        self.indegree[v]+=1
        
       

    def topoSortKahnsAlgo(self,n):
        # O (V+E) 
        topological_order=[]
        zero_set=[] #play around with any DS! 

        #add all vertices whose indegree=0
        for i in range(1,n+1):
            if(self.indegree[i]==0):
                zero_set.append(i)


        while zero_set:
            u=zero_set.pop() 
            topological_order.append(u)
            for v in self.neighbours[u]:
                self.indegree[v]-=1
                if(self.indegree[v]==0):
                    zero_set.append(v)


        if(len(topological_order)!=n):
            print("Graph contains cycle!")
            topological_order.clear()
            return []
        return topological_order #DAG


n=6
g=Graph(n)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,6)
g.addEdge(5,6)

print(g.topoSortKahnsAlgo(n))
