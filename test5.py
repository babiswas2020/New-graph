class Cell:
    def __init__(self,x,y,dist):
        self.x=x
        self.y=y
        self.dist=dist

def is_valid(x,y,M,N):
    if x<0 or x>=N:
       return False
    if y<0 or y>=N:
       return False
    if M[x][y]==0:
       return False
    return True

def mark_island(M,i,j,visited,N):
    dx=[0,0,1,-1,1,1,-1,-1]
    dy=[1,-1,0,0,1,-1,1,-1]
    queue=[]
    queue.append(Cell(i,j,0))
    visited[i][j]=True
    while queue:
        m=queue.pop(0)
        for k in range(8):
           X=dx[k]+m.x
           Y=dy[k]+m.y
           if is_valid(X,Y,M,N) and visited[X][Y]==False:
              queue.append(Cell(X,Y,m.dist+1))
              visited[X][Y]=True

def count_island():
    count=0
    M=[[1,1,0,0,0],[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,1,1,0]]
    visited=[[False for i in range(5)] for i in range(5)]
    for i in range(5):
       for j in range(5):
          if M[i][j]==1 and visited[i][j]==False:
             mark_island(M,i,j,visited,5)
             count=count+1
    return count

if __name__=="__main__":
   print(count_island())

   


      
    
