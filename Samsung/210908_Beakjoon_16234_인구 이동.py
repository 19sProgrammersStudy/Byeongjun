from collections import deque

def bfs(a,b):
    global l,r
    dq=deque()
    dq.append([a,b])
    person=[[a,b]]
    total=0
    while dq :
        x,y=dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if check[nx][ny] == 0 and l <= abs(board[nx][ny] - board[x][y]) <= r:
                    check[nx][ny] = 1
                    dq.append([nx,ny])
                    person.append([nx,ny])
    for i in range(len(person)):
        total+=board[person[i][0]][person[i][1]]
    for i in range(len(person)):
        board[person[i][0]][person[i][1]]=total//len(person)

    return len(person)

dx,dy=[-1,0,1,0],[0,1,0,-1]
n,l,r=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
answer=0
while True :
    #board_copy=board[:]
    uni_count=0
    check=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j]==0 :
                check[i][j]=1
                length= bfs(i,j)
                if int(length)>1 :
                    uni_count+=1
    if uni_count==0 :
        break
    #board=board_copy[:]
    answer+=1
print(answer)
