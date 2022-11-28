from collections import deque
# - n m  크기의 직사각형 형태 미로에 갇힘
# - 미로는 여러 마리 괴물이 있어 피해 탈출해야함
# - 동빈이 시작위치 1,1 이며 미로 출구는 n,m의 위치에 존재 한번에 한칸씩 이동
# - 이때 괴물이 있는 부분은 0 없는 부분은 1
# - 미로는 반드시 탈출할수 있는 형태로 제시
# - 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수
# - 칸을 셀때는 시작 칸과 마지막 칸 모두 포함해서 계산
#출력 10
n=5
m=6
escCount = 1 
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]



def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        print(queue)
        x,y = queue.popleft()
        # print("({0},{1}) 값={2}".format(x,y,graph[x][y]))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #벗어나면 무시
            if nx<0 or nx >= n or ny < 0 or ny>= m:
                continue
            #벽인경우 무시
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))