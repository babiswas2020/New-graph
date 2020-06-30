def is_valid(x,y,M,N,P):
    if x<0 or x>=P:
       return False
    if y<0 or y>=N:
       return False
    if M[x][y]==0:
       return False
    return True

def mark_island(M,i,j,visited,N,P,count):
    dx=[1,1,0,0,-1,1,-1,-1]
    dy=[1,-1,1,-1,0,0,1,-1]
    visited[i][j]=True
    count[0]=count[0]+1
    for k in range(8):
        X=dx[k]+i
        Y=dy[k]+j
        if is_valid(X,Y,M,N,P) and visited[X][Y]==False:
           mark_island(M,X,Y,visited,N,P,count)

def find_largest_island():
    largest=-1
    M=[[0,0,1,1,0],[1,0,1,1,0],[0,1,0,0,0],[0,0,0,0,1]]
    visited=[[False for i in range(5)] for j in range(4)]
    count=[0]
    for i in range(4):
       for j in range(5):
          if M[i][j]==1 and visited[i][j]==False:
             mark_island(M,i,j,visited,5,4,count)
          if largest<count[0]:
             largest=count[0]
             count[0]=0
    return largest

if __name__=="__main__":
   print(find_largest_island())



             

    

          
