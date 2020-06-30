from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)

   def DFS(self,visited,u,stack):
       visited[u]=True
       stack.append(u)
       for i in self.graph[u]:
          if not visited[i]:
             self.DFS(visited,i,stack)
       print(stack)
       stack.pop()
       visited[u]=False

if __name__=="__main__":
   graph=Graph(4)
   visited=[False]*graph.vertex
   stack=[]
   graph.add_edges(0,2)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(0,1)
   graph.DFS(visited,2,stack)
    
   

       
       