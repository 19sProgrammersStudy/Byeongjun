#Beakjoon_16236_아기상어
#https://www.acmicpc.net/problem/16236

from collections import deque
dx,dy=[-1,0,1,0],[0,1,0,-1]
n=int(input())
size,count,x,y,answer=2,0,0,0,0
board=[list(map(int,input().split())) for _ in range(n)]
fish=[]
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j]==9 :
            x,y=i,j
            board[i][j]=0

while True :
    dq=deque()
    dq.append((x,y,0))
    min_lst=[]
    min_length =1000000
    check=[[0]*n for _ in range(n)]
    while dq:
        xx, yy, cnt = dq.popleft()
        if cnt>min_length : break
        for i in range(4) :
            nx, ny=xx+dx[i],yy+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]<=size and check[nx][ny]==0 :
                dq.append((nx,ny,cnt+1))
                check[nx][ny]=1
                if  0<board[nx][ny]<size and min_length>=cnt+1 :
                    min_lst.append((nx,ny))
                    min_length=cnt+1
    if min_lst :
        min_lst.sort()
        answer+=min_length
        x,y=min_lst[0][0],min_lst[0][1]
        board[x][y]=0
        count+=1
        if size==count :
            size+=1
            count=0
    else : break

print(answer)

