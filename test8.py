from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
      self.graph[u].append(v)
      self.graph[v].append(u)

   def is_same_path(self,intime,outtime,u,v):
       if ((intime[u]<intime[v]) and (outtime[u]>outtime[v])) or ((intime[v]<intime[u]) and (outtime[v]>outtime[u])):
          return True
       else:
          return False

   def DFS(self,u,timer,intime,outtime,visited):
       timer[0]=timer[0]+1
       intime[u]=timer[0]
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             self.DFS(i,timer,intime,outtime,visited)
       timer[0]=timer[0]+1
       outtime[u]=timer[0]

if __name__=="__main__":
   graph=Graph(8)
   graph.add_edges(1,2)
   graph.add_edges(2,5)
   graph.add_edges(1,3)
   graph.add_edges(3,6)
   graph.add_edges(1,4)
   graph.add_edges(4,7)
   intime=[0]*graph.vertex
   outtime=[0]*graph.vertex
   timer=[0]
   visited=[False]*graph.vertex
   graph.DFS(1,timer,intime,outtime,visited)
   print(intime)
   print(outtime)
   print(graph.is_same_path(intime,outtime,2,6))
   print(graph.is_same_path(intime,outtime,2,5))
   print(graph.is_same_path(intime,outtime,6,3))



   
       
       