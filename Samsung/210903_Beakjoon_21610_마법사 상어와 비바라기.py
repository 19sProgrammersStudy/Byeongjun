#Beakjoon_21610_마법사 상어와 파이어볼
#https://www.acmicpc.net/problem/21610

from collections import deque
def wind(x,y,dir,speed):
    global dx,dy,n
    nx, ny = x + speed * dx[dir], y + speed * dy[dir]
    if nx<0 :
        nx=n-(abs(nx)%n)
        if nx==n : nx=0
    else : nx=nx%n
    if ny<0 :
        ny=n-(abs(ny)%n)
        if ny == n : ny = 0
    else :ny=ny%n
    return [nx, ny]
    nx = (x + dx[dir] * speed) % n
    ny = (y + dy[dir] * speed) % n

    return [nx,ny]

#시간초과로 인한 주석처리
""" def check(xy):
    global cloud
    if xy in cloud :
        return False
    return True
"""
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
move=deque()
cloud=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
for i in range(m) :
    d,s=map(int,input().split())
    move.append([d-1,s])
while move :
    lst=[[0]*n for _ in range(n)]
    dir,speed=move.popleft()
    for i in range(len(cloud)):
        cloud[i]=wind(cloud[i][0],cloud[i][1],dir,speed)
    for i in range(len(cloud)) :
        board[cloud[i][0]][cloud[i][1]]+=1
        lst[cloud[i][0]][cloud[i][1]]=1
    for i in range(len(cloud)):
        count=0
        checkx,checky=[-1,-1,1,1],[-1,1,1,-1]
        for j in range(4) :
            nx,ny=cloud[i][0]+checkx[j],cloud[i][1]+checky[j]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]!=0 :
                count+=1
        board[cloud[i][0]][cloud[i][1]] +=count
    temp=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]>=2 and lst[i][j]!=1:
                temp.append([i,j])
                board[i][j]-=2
    cloud=temp[:]

answer=0
for i in board :
    answer+=sum(i)

print(answer)