#Beakjoon_17144_미세먼지 안녕
#https://www.acmicpc.net/problem/17144

r,c,t=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(r)]
dr,dc=[-1,0,1,0],[0,1,0,-1]
marchine=[]

for i in range(len(board)):
    if board[i][0]==-1 :
        marchine.append([i,0])

for i in range(t) :
    #분산하기
    spreed=[[0]*c for _ in range(r)]
    for j in range(len(board)):
        for k in range(len(board[j])):
            count = 0
            if board[j][k]!=0 and board[j][k]!=-1 :
                spreed_amount = int(board[j][k]/5)
                for l in range(4) :
                    nr,nc=j+dr[l],k+dc[l]
                    if 0<=nr<r and 0<=nc<c and board[nr][nc]!=-1 :
                        spreed[nr][nc]+=spreed_amount
                        count+=1
                spreed[j][k]+=board[j][k]-int(board[j][k]/5)*count
    for j in range(2):
        spreed[marchine[j][0]][marchine[j][1]]=-1
    board=spreed[:]

    #공기청정기 가동
    #위부터
    x=marchine[0][0]
    for j in range(x-1,0,-1):
        board[j][0]=board[j-1][0]
    board[0][:c-1] =board[0][1:c]
    for j in range(x):
        board[j][c-1]=board[j+1][c-1]
    board[x][2:]=board[x][1:c-1]
    board[x][1]=0
    #아래쪽
    x = marchine[1][0]
    for j in range(x+1,r-1,1):
        board[j][0]=board[j+1][0]
    board[r-1][:c-1]=board[r-1][1:c]
    for j in range(r-1,x-1,-1):
        board[j][c-1]=board[j-1][c-1]
    board[x][2:] = board[x][1:c - 1]
    board[x][1] = 0

answer=0
for i in range(r):
    answer+=sum(board[i])
print(answer+2)
