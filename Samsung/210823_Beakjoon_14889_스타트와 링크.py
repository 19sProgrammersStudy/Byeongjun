#Beakjoon_14889_스타트와 링크
#https://www.acmicpc.net/problem/14889

from itertools import combinations as cb
from itertools import permutations as per
n=int(input())
score=[list(map(int,input().split())) for _ in range(n)]
com=list(cb([i for i in range(n)],n//2))
min=10000
for i in range(len(com)//2) :
    start,link=list(per(com[i],2)),list(per(com[-1-i],2))
    startsum,linksum=0,0
    for j in range(len(start)) :
        startsum+=score[start[j][0]][start[j][1]]
        linksum+=score[link[j][0]][link[j][1]]
    if abs(startsum-linksum) < min : min = abs(startsum-linksum)

print(min)