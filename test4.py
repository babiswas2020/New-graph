from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def IDS_util(self,src,destn,maxdepth):
       if src==destn:
          return True
       if maxdepth<=0:
          return False
       for i in self.graph[src]:
          if self.IDS_util(i,destn,maxdepth-1):
             return True
       return False

   def IDS(self,src,destn,maxdepth):
       for i in range(maxdepth):
           if self.IDS_util(src,destn,i):
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
   traget=6
   maxdepth=2
   src=0
   print(graph.IDS(0,6,2))
