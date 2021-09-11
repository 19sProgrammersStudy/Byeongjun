#Beakjoon_20057_마법사 상어와 토네이도
#https://www.acmicpc.net/problem/20057

from copy import deepcopy
def turn(dirc) :
    if dirc==3 : next=0
    else : next=dirc+1
    return next
def spreed(x,y,dir) :
    if dir==0 : return [[x-1,y+1],[x+1,y+1],[x-2,y],[x-1,y],[x+1,y],[x+2,y],[x-1,y-1],[x+1,y-1],[x,y-2]]
    elif dir==1 : return [[x-1,y-1],[x-1,y+1],[x,y-2],[x,y-1],[x,y+1],[x,y+2],[x+1,y-1],[x+1,y+1],[x+2,y]]
    elif dir==2 : return [[x-1,y-1],[x+1,y-1],[x-2,y],[x-1,y],[x+1,y],[x+2,y],[x-1,y+1],[x+1,y+1],[x,y+2]]
    else : return [[x+1,y-1],[x+1,y+1],[x,y-2],[x,y-1],[x,y+1],[x,y+2],[x-1,y-1],[x-1,y+1],[x-2,y]]
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
cal=deepcopy(board)
x,y,dir=int(n/2),int(n/2),0
distance=1
per=[0.01,0.01,0.02,0.07,0.07,0.02,0.1,0.1,0.05]
answer=0
dx,dy=[0,1,0,-1],[-1,0,1,0]
flag=True
while flag :
    for i in range(2) :
        if x == 0 and y == 0:
            flag = False
            break
        for j in range(distance):
            nx,ny=x+dx[dir],y+dy[dir]
            if board[nx][ny]!=0 :
                temp=spreed(nx,ny,dir)
                sp=0
                for i in range(len(per)) :
                    sp+=int(board[nx][ny]*per[i])
                ax,ay,a=nx+dx[dir],ny+dy[dir],board[nx][ny]-sp
                for k in range(len(temp)) :
                    if 0<=temp[k][0]<n and 0<=temp[k][1]<n :
                        board[temp[k][0]][temp[k][1]]+= int(board[nx][ny]*per[k])
                    else :
                        answer+=int(board[nx][ny]*per[k])
                if 0<=ax<n and 0<=ay<n :
                    board[ax][ay] += a
                else : answer+=a
            board[nx][ny]=0
            x,y=nx,ny
        dir=turn(dir)
    distance= distance+1 if distance<n-1 else distance
print(answer)

