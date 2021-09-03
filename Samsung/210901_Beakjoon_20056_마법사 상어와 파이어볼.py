#Beakjoon_20056_마법사 상어와 파이어볼
#https://www.acmicpc.net/problem/20056

from collections import deque
dx,dy=[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
n,m,k=map(int,input().split())
dq=deque()
for i in range(m) :
    r,c,m,s,d =map(int,input().split())
    dq.append([r-1,c-1,m,s,d])
for i in range(k) :
    board=[[deque() for _ in range(n)] for _ in range(n)]
    while dq :
        r, c, m, s, d = dq.popleft()
        nr,nc=r+s*(dx[d]),c+s*(dy[d])
        #if nr>=n : nr=nr-n
        #if nc>=n : nc=nc-n
        #if nr<0 : nr=n-abs(nr)
        #if nc<0 : nc=n-abs(nc)
        nr = (nr + n) % n
        nc = (nc + n) % n

        board[nr][nc].append([m,s,d])
    for j in range(len(board)):
        for k in range(len(board[j])):
            seperate = [0, 0]
            dir=[]
            if len(board[j][k])==1 :
                m, s, d = board[j][k].popleft()
                dq.append([j,k,m,s,d])
            elif len(board[j][k])>1 :
                while board[j][k] :
                    r,c,m=board[j][k].popleft()
                    seperate[0]+=r
                    seperate[1]+=c
                    dir.append(0 if m%2==0 else 1)
                seperate[0]//=5
                seperate[1]//=len(dir)
                if seperate[0]!=0 :
                    if len(dir)==dir.count(0) or len(dir)==dir.count(1) :
                        dq.append([j,k,seperate[0],seperate[1],0])
                        dq.append([j, k, seperate[0], seperate[1], 2])
                        dq.append([j, k, seperate[0], seperate[1], 4])
                        dq.append([j, k, seperate[0], seperate[1], 6])
                    else :
                        dq.append([j, k, seperate[0], seperate[1], 1])
                        dq.append([j, k, seperate[0], seperate[1], 3])
                        dq.append([j, k, seperate[0], seperate[1], 5])
                        dq.append([j, k, seperate[0], seperate[1], 7])
answer=0
while dq :
    r, c, m, s, d =dq.popleft()
    answer+=m

print(answer)