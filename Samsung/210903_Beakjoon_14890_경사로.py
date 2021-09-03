#Beakjoon_14890_경사로
#https://www.acmicpc.net/problem/14890

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
count=0
for i in range(n):
    temp=[]
    for j in range(n) :
        temp.append(board[j][i])
    board.append(temp)
for i in board :
    idx=0
    check=[0]*n
    while idx<n-1 :
        if i[idx]==i[idx+1] : idx+=1
        elif i[idx+1]-i[idx]==1 :
            flag=True
            now=i[idx]
            for j in range(idx,idx-m,-1):
                if j<0 or i[j]!=now or check[j]==1:
                    flag=False
                    break
            if flag :
                check[idx-m+1:idx+1]=[1]*m
                idx += 1
            else : break
        elif i[idx]-i[idx+1] ==1 :
            flag = True
            now = i[idx+1]
            for j in range(idx+1,idx+m+1,1):
                if j>=n or i[j]!=now or check[j]==1:
                    flag=False
                    break
            if flag :
                check[idx+1:idx+m]=[1]*m
                idx+=m
            else:
                break
        else :
            break
    if idx==n-1 : count+=1
print(count)