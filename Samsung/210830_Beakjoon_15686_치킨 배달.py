#Beakjoon_15686_치킨 배달
#https://www.acmicpc.net/problem/15686

from itertools import combinations as cb
n,m=map(int,input().split())
min_range=1000000000
map=[list(map(int,input().split())) for _ in range(n)]
chicken=[]
home=[]
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j]==2 :
            chicken.append([i,j])
        elif map[i][j]==1 :
            home.append([i,j])
comb=tuple(cb(chicken,m))
for i in comb :
    total=0
    for j in home :
        range = 1000000000
        for k in i :
            temp=abs(j[0]-k[0])+abs(j[1]-k[1])
            if temp<range : range=temp
        total+=range
    if total<min_range : min_range=total

print(min_range)




