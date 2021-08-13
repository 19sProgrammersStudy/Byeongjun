#레벨2.[1차]프렌즈4블록
#https://programmers.co.kr/learn/courses/30/lessons/17679?language=python3

from collections import deque
def drop(lst):
    for i in range(len(lst[0])):
        dq=deque()
        cnt=0
        for j in range(len(lst)):
            if lst[j][i] != "X":
                dq.append(lst[j][i])
            else : cnt +=1
        for j in range(len(lst)) :
            if cnt!=0 :
                lst[j][i]="X"
                cnt-=1
            else :  lst[j][i]=dq.popleft()
    return lst


def check(temp):
    count = 0
    for i in temp:
        count += i.count(1)
    return count


def solution(m, n, board):
    answer = 0
    flag = True
    picture = [[j for j in i] for i in board]
    while flag :
        temp = [[0] * n for _ in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                if (picture[i][j] == picture[i][j + 1] == picture[i + 1][j] == picture[i + 1][j + 1]) and picture[i][j]!="X":
                    temp[i][j], temp[i][j + 1], temp[i + 1][j], temp[i + 1][j + 1] = 1, 1, 1, 1
        count = check(temp)
        if count != 0:
            for i in range(m):
                for j in range(n):
                    if temp[i][j] == 1: picture[i][j] = "X"
            picture = drop(picture)
            answer += count
        else:
            flag=False

    return answer
