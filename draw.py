#그림 전체를 돌아야함
from collections import deque

#세로
N = 6
#가로
M = 5
graph = [
    [1,1,0,1,1],
    [0,1,1,1,1],
    [0,0,0,0,1],
    [1,0,0,1,1],
    [0,0,1,1,1],
    [1,1,1,1,1]
]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
countList=[]
def bfs(y,x):
    count=0
    q = deque()
    q.append((y,x))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx < 0 or nx >= M or ny < 0 or ny>= N:
                continue
            elif graph[ny][nx]==0:
                continue
            elif graph[ny][nx]==1 or graph[y][x]==1:
                graph[ny][nx]=0
                q.append((nx,ny))
                count+=1

    if(count!=0):
        countList.append(count)


        




for i in range(N):
    for j in range(M):
        # if graph[i][j]!=0:   
        #     print("i:{} j:{}".format(i,j))
        bfs(j,i)
print(len(countList))
print(max(countList))




for i in graph:
    print(i)