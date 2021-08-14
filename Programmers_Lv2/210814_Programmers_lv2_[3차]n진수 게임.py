#레벨2.[3차]n진수 게임
#https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3

from collections import deque
def solution(n, t, m, p):
    answer = ''
    lst=["0"]
    now=1
    while len(lst)< t*m :
        temp=now
        templi=deque()
        while temp > 0 :
            if temp%n <10 :
                templi.append(str(temp%n))
            elif temp%n == 10 :
                templi.append("A")
            elif temp%n == 11 :
                templi.append("B")
            elif temp%n == 12 :
                templi.append("C")
            elif temp%n == 13 :
                templi.append("D")
            elif temp%n == 14 :
                templi.append("E")
            elif temp%n == 15 :
                templi.append("F")
            temp//=n
        while templi :
            lst.append(templi.pop())
        now+=1
    idx=p-1
    while len(answer)<t :
        answer+=lst[idx]
        idx+=m
    return answer