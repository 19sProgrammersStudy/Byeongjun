#Beakjoon_14502_연구소
#https://www.acmicpc.net/problem/14502

from itertools import combinations as cb
import copy
from collections import deque
def bfs(arr) :
    dq=deque()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==2 :
                dq.append((i,j))
    while dq :
        x,y=dq.popleft()
        for i in range(4) :
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny] == 0 :
                    dq.append((nx,ny))
                    arr[nx][ny]=2
    count=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0: count+=1
    return count

mx=0
dx,dy=[-1,0,1,0],[0,1,0,-1]
n,m=map(int,input().split(" "))
lab=[list(map(int,input().split(" "))) for _ in range(n)]
wall=[]
for i in range(len(lab)) :
    for j in range(len(lab[i])) :
        if lab[i][j]==0 :  wall.append((i,j))
for i in cb(wall,3):
    round=copy.deepcopy(lab)
    for j in range(3):
        round[i[j][0]][i[j][1]]=1
    safe=bfs(round)
    if safe>mx :
        mx=safe

print(mx)