from collections import deque
from copy import deepcopy
def bfs(a,b) :
    global board,n
    dq=deque()
    dq.append([a,b])
    cnt=1
    while dq :
        x,y=dq.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<2**n and 0<=ny<2**n and board[nx][ny]!=0 and check[nx][ny]==0 :
                dq.append([nx,ny])
                check[nx][ny]=1
                cnt+=1
    return cnt

n,q=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(2**n)]
qlist=list(map(int,input().split()))
dx,dy=[-1,0,1,0],[0,1,0,-1]

for s in range(len(qlist)):
    size=qlist[s]
    #size가 0이면 이전과 동일
    #회전로직
    temp = [[0] * (2 ** n) for i in range(2 ** n)]
    idx1=0
    print(temp)
    while idx1<len(board):
        idx2=0
        while idx2<len(board):
            line=idx2+(2**size)-1
            for i in range(2**size):
                idx3 = 0
                round=board[idx1+i][idx2:idx2+(2**size)]
            #for i in range(idx2+(2**size)-1,idx1-1,-1):
                for j in range(idx1,idx1+(2**size)):
                    temp[j][line]=round[idx3]
                    idx3+=1
                line-=1
            idx2+=2**size
        idx1+=2**size
    board=deepcopy(temp)
    print(temp)
    print(board)
    #얼음 양 줄이기
    for i in range(len(board)):
        for j in range(len(board)):
            cnt=0
            for k in range(4) :
                nx,ny=i+dx[k],j+dy[k]
                if 0<=nx<len(board) and 0<=ny<len(board) and temp[nx][ny]!=0 :
                    cnt+=1
            if cnt<3 and temp[i][j]!=0 : board[i][j]-=1
#덩어리 찾기
check=[[0]*(2**n) for i in range(2**n)]
max=0
summation=0
for i in range(len(board)):
    for j in range(len(board)) :
        if check[i][j]== 0 and board[i][j]!=0 :
            check[i][j]=1
            merge=bfs(i,j)
            if merge>max :
                max=merge
        summation+=board[i][j]
print(summation)
if max!=0:print(max)
else : print(0)