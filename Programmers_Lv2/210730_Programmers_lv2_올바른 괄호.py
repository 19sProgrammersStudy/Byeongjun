#레벨2.올바른 괄호
#https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3

from collections import deque
def solution(s):
    dq=deque()
    answer = True
    for i in s : 
        if i == "(" :
            dq.append(i)
        else : 
            if dq and dq[-1]=="(" : 
                dq.pop()
            else : 
                dq.append(i)
    if dq : answer=False
    return answer