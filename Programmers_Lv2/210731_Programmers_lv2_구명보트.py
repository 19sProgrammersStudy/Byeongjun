#레벨2.구명보트
#https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    dq=deque(people)
    answer=0
    while dq : 
        boat=0
        boat+=dq[0]
        dq.popleft()
        if dq and boat+dq[-1] <=limit  : 
            boat+=dq[-1]
            dq.pop()
        answer+=1
    return answer