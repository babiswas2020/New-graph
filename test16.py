from collections import defaultdict

class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)
   def add_edges(self,u,v):
      self.graph[u].append(v)
      self.graph[v].append(u)
   def is_cyclic(self,visited,u,parent):
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             if self.is_cyclic(visited,i,u):
                 return True
          elif i!=parent:
             return True
       return False
   def is_tree(self):
      status=False
      visited=[False]*self.vertex
      for i in range(self.vertex):
         if not visited[i]:
            if self.is_cyclic(visited,i,-1):
               status=True
               break
      if status:
         print("The graph is not tree")
      else:
         print("The graph is tree")

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(4,1)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.is_tree()


      
      
            
