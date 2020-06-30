from collections import defaultdict
import sys

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def IDS_util(self,src,target,depth):
       if src==target:
          return True
       if depth<=0:
          return False
       for i in self.graph[src]:
          if self.IDS_util(i,target,depth-1):
             return True
       return False

   def IDS(self,src,target,depth):
       for i in range(depth):
           if self.IDS_util(src,target,depth):
              return True
       return False

if __name__=="__main__":
   graph=Graph(7)
   graph.add_edges(0,1)
   graph.add_edges(0,2)
   graph.add_edges(1,3)
   graph.add_edges(1,4)
   graph.add_edges(2,5)
   graph.add_edges(2,6)
   print(graph.IDS(0,6,int(sys.argv[1])))
