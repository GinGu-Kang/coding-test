from collections import deque
#특정거리 도시찾기
#어떤 나라에는 1 ~ n번까지의 도시와 M 개의 단방향 도로 존재
#모든 도로의 거리 1
#특정한 도시 X로부터 출발해 도달할 수 있는 모든 도시중 
#최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램 작성
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단거리는 항상 0 이라고 가정
#최소 최단거리 X면 출력 안함

#N개의 도시 M개의 도로 K의 최단거리 조건 출발 도시 X
#큐안에 집어넣고 현재도시 기억 1다음에 2가있고 2다음 3이있다면 count 1씩 올림 
# 최종으로 count 가 2 라면 현재 도시 출력
# x값을 v에 넣음 citymap 숫자가 v 면 카운트하고 그다음 숫자를 큐에 넣음 
# 큐에서 숫자를 빼서 v 에 넣고 현재 city 맵의 첫숫자가 v와 다르다면 통과 같다면 다음숫자를 v에 넣고 카운트
# 마지막에 카운트가 2이면 print


# 도시의 수만큼 반복?
# 전체 돌면서 앞이 1 인 행만 스택에 넣는다
# 
N,M,K,X = 4,4,2,1
cityMap = [
    [1,2]
    [1,3]
    [2,3]
    [2,4]
]

queue = deque(X)
count = 0
while queue:
    
    for city in cityMap:
        v = queue.popleft()
        if city[0]==v:
            queue.append(city[1])
            count+=1


