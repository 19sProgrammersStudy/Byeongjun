#Beakjoon_3190_뱀
#https://www.acmicpc.net/problem/3190

from collections import deque
def turn(dir,next) :
    if next=='L' :
        next_dir= dir-1 if dir>0 else 3
    else :
        next_dir = dir+1 if dir<3 else 0

    return next_dir

n,m=int(input()),int(input())
board=[[0]*n for _ in range(n)]
move=deque()
dx,dy=[-1,0,1,0],[0,1,0,-1]
for i in range(m) :
    x,y=map(int,input().split())
    board[x-1][y-1]=1
l=int(input())
for i in range(l):
    move.append(list(map(str,input().split())))
dq=deque()
dq.append([0,0])
dir=1
time=0
flag=True
while flag :
    time+=1
    x,y=dq[0][0],dq[0][1]
    nx,ny=x+dx[dir],y+dy[dir]
    if nx<0 or nx>=n or ny<0 or ny>=n : flag=False
    for i in dq :
        if i[0]==nx and i[1]==ny :
            flag=False
            break
    if flag==True :
        dq.appendleft([nx,ny])
        if board[nx][ny]==0 : dq.pop()
        else : board[nx][ny]=0
        if move and int(move[0][0])==time :
            dir=turn(dir,move[0][1])
            move.popleft()
print(time)

