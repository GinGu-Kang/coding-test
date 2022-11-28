

#한 좌표마다 방문처리 확인
#방문처리 안되어있으면 전체탐색 하고 count +=1
# 방문처리가 되어있거나 1일때 count x
# 끝날때까지 반복
# 들어갈때 현재 좌표 방문 처리
# 일단 들어가 쭊 들어간다음 1바꾸면서 나오기 
def dfs(x,y):
    global iceFrame
    
    if x <= -1 or x >= row or y <=-1 or  y >= col:
        return False
    print(y,",",x)
    if iceFrame[y][x]==0:
        iceFrame[y][x] = 1
        print(y,x,"방문")
        dfs(x,y-1) #상
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
    return False
# iceFrame=[
#     [0,0,1,1,0],
#     [0,0,0,1,1],
#     [1,1,1,1,1],
#     [0,0,0,0,0]
# ]

col =4
row = 5
count=0

iceFrame=[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

for y in range(col):
    for x in range(row):
        # print("x,y",y,",",x)
        if iceFrame[y][x] !=1:
            dfs(x,y)
            count+=1


# for x in iceFrame:
#     print(x)
print("까운트",count)    