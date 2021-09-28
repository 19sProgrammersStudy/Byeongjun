from copy import deepcopy
n,m,t=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
dx,dy=[-1,0,1,0],[0,1,0,-1]
for T in range(t) :
    x,d,k=map(int,input().split())
    idx=x
    temp=board[:]
    while idx<len(board)+1:
        if d == 0 : temp[idx-1]= temp[idx-1][len(temp[idx-1])-k:]+temp[idx-1][:len(temp[idx-1])-k]
        else : temp[idx-1] = temp[idx-1][k:]+temp[idx-1][:k]
        idx+=x
    board=deepcopy(temp)
    count_all=0
    for i in range(n):
        for j in range(m) :
            if temp[i][j]!=0 :
                cnt=0
                for k in range(4) :
                    nx,ny=i+dx[k],j+dy[k]
                    if ny == -1:
                        ny = m - 1
                    elif ny == m:
                        ny = 0
                    if 0<=nx<n and 0<=ny<m :
                        if temp[i][j]==temp[nx][ny] :
                            board[nx][ny]=0
                            cnt+=1
                if cnt>0 :
                    count_all+=cnt
                    board[i][j]=0
    summation = 0
    notzero = 0
    if count_all==0 :
        for i in range(len(board)) :
            summation+=sum(board[i])
            notzero+=len(board[i])-(board[i].count(0))
        if summation==0 and notzero ==0 :
            std=0
        else : std=summation/notzero
        for i in range(n):
            for j in range(m) :
                if board[i][j]!=0 :
                    if std>board[i][j] :
                        board[i][j]+=1
                    elif std <board[i][j] : board[i][j]-=1
total=0
for i in range(len(board)) :
    total+=sum(board[i])
print(total)



