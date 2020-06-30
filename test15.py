from collections import defaultdict
class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)

   def tree(self,visited,u):
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             self.tree(visited,i)

   def count_trees(self):
      visited=[False]*self.vertex
      count=0
      for i in range(self.vertex):
          if not visited[i]:
             self.tree(visited,i)
             count=count+1
      return count

if __name__=="__main__":
   graph=Graph(5)
   graph.add_edges(0,1)
   graph.add_edges(0,2)
   graph.add_edges(3,4)
   print(graph.count_trees())
