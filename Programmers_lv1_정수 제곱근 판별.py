#레벨1.정수 제곱근 판별
#https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3

import math
def solution(n):
    x=int(math.sqrt(n))
    if x**2== n:
        answer=(x+1)*(x+1)
    else : 
        answer = -1
    return answer