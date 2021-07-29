#레벨2.짝지어 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3

from collections import deque
def solution(s):
    dq=deque()
    for i in s : 
        if dq and dq[-1] == i :
            dq.pop()
        else :
            dq.append(i)
    if dq : return 0
    return 1