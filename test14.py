from collections import defaultdict

class Graph:
    def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

    def add_edges(self,u,v):
        self.graph[u].append(v)


    def DFS_util(self,visited,u,value,minimum):
        visited[u]=True
        if minimum[0]>value[u]:
           minimum[0]=value[u]
        if u in self.graph:
          for i in self.graph[u]:
             if not visited[i]:
                self.DFS_util(visited,i,value,minimum)


    def DFS(self,value):
      visited=[False]*self.vertex
      minimum=[50000000]
      accumulator=0 
      for i in range(self.vertex):
          if not visited[i]:
             self.DFS_util(visited,i,value,minimum)
             accumulator+=minimum[0]
             minimum[0]=5000000
      print(accumulator)

if __name__=="__main__":
   arr=[0,1,6,2,7,3,8,4,9,5,10]
   graph=Graph(11)
   graph.add_edges(1,2)
   graph.add_edges(3,4)
   graph.add_edges(5,6)
   graph.add_edges(7,8)
   graph.add_edges(9,10)
   graph.DFS(arr)
   print("Another Sum of minimum elements")
   arr=[0,2,5,3,4,8]
   graph=Graph(6)
   graph.add_edges(1,4)
   graph.add_edges(4,5)
   graph.DFS(arr)


   
    