#Beakjoon_14503_로봇 청소기
#https://www.acmicpc.net/problem/14503

from collections import deque
def round(dir) :
    if dir==0 : dir=3
    else : dir-=1
    return dir
def bfs(now_x,now_y,dir) :
    global clean,house
    dq=deque()
    dq.append((now_x,now_y))
    while dq :
        count=0
        nx,ny=dq.popleft()
        for i in range(4) :
            dir=round(dir)
            next_x,next_y=nx+dx[dir],ny+dy[dir]
            if 0<=next_x<n and 0<=next_y<m :
                if house[next_x][next_y]==0 :
                    dq.append((next_x,next_y))
                    house[next_x][next_y]=2
                    clean+=1
                    break
                else : count+=1
        if count==4 :
            if 0<=nx+dx[dir-2]<n and 0<=ny+dy[dir-2]<m and house[nx+dx[dir-2]][ny+dy[dir-2]]!=1 :
                dq.append((nx+dx[dir-2],ny+dy[dir-2]))
            else : return

n,m=map(int,input().split())
x,y,dir=map(int,input().split())
house=[list(map(int,input().split())) for _ in range(n)]
dx,dy=[-1,0,1,0],[0,1,0,-1]
clean=1
house[x][y]=2
bfs(x,y,dir)
for i in range(len(house)):
    print(house[i])
print(clean)