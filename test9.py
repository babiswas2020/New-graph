from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)

   def DFS(self,stack,u,visited):
       stack.append(u)
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             self.DFS(stack,i,visited)
       print(stack)
       stack.pop()

if __name__=="__main__":
   graph=Graph(14)
   graph.add_edges(1,2)
   graph.add_edges(1,3)
   graph.add_edges(1,4)
   graph.add_edges(2,5)
   graph.add_edges(2,6)
   graph.add_edges(2,8)
   graph.add_edges(3,9)
   graph.add_edges(3,10)
   graph.add_edges(4,11)
   graph.add_edges(5,12)
   graph.add_edges(5,13)
   graph.add_edges(3,0)
   visited=[False]*graph.vertex
   stack=[]
   graph.DFS(stack,1,visited)


       