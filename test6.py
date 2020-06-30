def is_valid(x,y,M,N):
    if x<0 or x>=N:
       return False
    if y<0 or y>=N:
       return False
    if M[x][y]==0:
       return False
    return True


def mark_island(M,i,j,visited,N):
   dx=[1,-1,1,-1,0,0,1,-1]
   dy=[1,-1,-1,1,1,-1,0,0]
   visited[i][j]=True
   for k in range(8):
      X=i+dx[k]
      Y=j+dy[k]
      if is_valid(X,Y,M,N) and visited[X][Y]==False:
         mark_island(M,X,Y,visited,N)

def count_island():
   M=[[1,1,0,0,0],[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,1,1,0]]
   count=0
   visited=[[False for i in range(5)]for i in range(5)]
   for i in range(5):
     for j in range(5):
        if visited[i][j]==False and M[i][j]==1:
           mark_island(M,i,j,visited,5)
           count=count+1
   return count

if __name__=="__main__":
  print(count_island())

           


