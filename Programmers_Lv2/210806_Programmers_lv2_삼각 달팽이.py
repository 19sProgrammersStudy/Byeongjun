#레벨2.삼각 달팽이
#https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3

def solution(n):
    lst=[[0]*n for _ in range(n)]
    startx,starty=0,0
    num=1
    check=0
    for i in range(1,n+1) :
        check+=i
    answer = []
    while num<=check :
        for i in range(starty,len(lst)) :
            if lst[i][startx]!=0 or num>check : break
            lst[i][startx]=num
            num+=1
            starty+=1
        starty-=1
        startx+=1
        for j in range(startx,len(lst)) :
            if lst[starty][j]!=0 or num>check : break
            lst[starty][j]=num
            num+=1
            startx+=1
        startx-=2
        starty-=1
        temp=startx
        for k in range(temp,0,-1) :
            if lst[starty][startx]!=0 or num>check : break
            lst[starty][startx]=num
            num+=1
            startx-=1
            starty-=1
        starty+=2
        startx+=1

    for i in range(len(lst)) :
        for j in range(len(lst)) :
            if lst[i][j]!=0 : answer.append(lst[i][j])

    return answer
