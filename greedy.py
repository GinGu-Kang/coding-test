import time
from collections import deque


def changeMoney():
    n=1260
    count =0


    conint_types =[500,100,50,10]
    for coin in conint_types:
        
        print(int(n/coin),end="")
        
        n%=coin            
def largeNumber():

    # #map은 요소하나하나를 변환 시켜주는것
    # numRange,addNum,limitNum = map(int,(input().split()))
    # data = list(map(int,input().split()))

    numRange = 5
    addNum = 7
    limitNum = 2
    data = [3,4,3,4,3]
    addCount = 0 

    result = 0


    data.sort()
    if(numRange>=len(data)):
        for index in range(addNum):
            if addCount < limitNum:
                result+=data[-1]
                addCount+=1
            else:
                result+=data[-2]
                addCount = 0
            print(result)
        
    
        
        

def make1():
    result=0
    n = 25
    k= 3
    
    while (n!=1):
        
        if(n%k!=0):
            n-=1
            result+=1
        else:
            n =n/k
            result+=1
    print(result)
    

def travle():
    size= 5
    plan = "R R R U D D".split()
    coordinate = [1,1]

    for direction in plan:
        if direction == "L":
            if coordinate[1] > 1:
                coordinate[1]-=1

        elif direction == "R":
            if(coordinate[1] < size):
                coordinate[1]+=1

        elif direction == "U":
            if(coordinate[0] > 1):
                coordinate[0]-=1

        elif direction == "D":
            if(coordinate[0] < size):
                coordinate[0]+=1

        print(coordinate)




def queue():
    queue = deque()

    queue.append(1)
    queue.append(2)
    queue.append(3)
    a=queue.popleft()
    print(a)
    queue.reverse()
    print(queue)

def dfs(graph,v,visited):
    visited[v] = True   #들어온것은 True
    print(v, end = ' ') #현재 노드 출력
    for i in graph[v]:  #현재 그래프 차례로 출력
        if not visited[i]:   #현재 출력된 노드가 방문이 안되었다면 dfs 다시 실행
            dfs(graph,i,visited)   



#현재 나랑 방문한 노드를 다집어넣어
#탐색 끝났으면 맨첫번째꺼버려
# 두번째노드로 가 
# 1,2,3,8,7,
# 시작 , 1번 가서 끝까지 print 출력하고 방문 
# 
def bfs(graph,start,visited):
    queue = deque([start])

    visited[start]=True
    while queue:
        v=queue.popleft()
        
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True



def fsMain():
    #dfs 결과 1 2 7 6 8 3 4 5
    #bfs 결과 1,2,3,8,7,4,5,6
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    visited = [False] * 9 

    bfs(graph,1,visited)







    



start_time = time.time()
# 시작
fsMain()
# 소요시간 출력
end_time = time.time()
print("\ntime:",end_time-start_time)
