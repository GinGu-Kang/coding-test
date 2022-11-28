from collections import deque


# 레이더 만들기
def solution(places):
    answer = []
    N=5
    limDis = 2
    dx = [-2,-1,1,2,0,0,0,0]
    dy = [0,0,0,0,-2,-1,1,2]
    direction = ["좌","좌","우","우","하","하","상","상"]
    place = ["POOOP",
             "OXXOX",
             "OPXPX",
             "OOXOX",
             "POXXP"]
    count=0
    for x in range(5):
        for y in range(5):

            
            isFailed = False

            if place[x][y] == "P":
                place[x][y].replace("P","X")
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # nD = direction[i]
                    #벗어나면 무시
                    if nx<0 or nx >= N or ny < 0 or ny>= N:
                        continue
                    if place[nx][ny] =="P":
                        isFailed=True
                        continue
            if isFailed:
                print("거리안지킴")
                for a in place:
                    print(a)
                isFailed=False
    return answer

solution("a")