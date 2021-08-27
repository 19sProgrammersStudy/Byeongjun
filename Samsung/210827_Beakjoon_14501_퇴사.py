#Beakjoon_14501_연산자 끼워넣기
#https://www.acmicpc.net/problem/14501

def dfs(idx,earn) :
    global n,mx,mx_earn,schedule
    if idx>=n :
       if mx_earn<earn : mx_earn=earn
    for i in range(idx,n):
        if i+schedule[i][0]<=n :
            dfs(i+schedule[i][0],earn+schedule[i][1])
        else :
            dfs(i + schedule[i][0], earn)

n=int(input())
schedule=[list(map(int,input().split())) for _ in range(n)]
mx,mx_earn=0,0
dfs(0,0)
print(mx_earn)