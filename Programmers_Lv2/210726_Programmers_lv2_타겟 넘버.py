#레벨2.타겟 넘버
#https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

from collections import deque
def solution(numbers, target):
    #초기화
    dq=deque(0 for _ in range(1))
    
    for i in numbers :
        temp = deque()
        while dq :
            num=dq.popleft()
            temp.append(num+i)
            temp.append(num-i)
        dq=temp
    answer = dq.count(target)
    return answer