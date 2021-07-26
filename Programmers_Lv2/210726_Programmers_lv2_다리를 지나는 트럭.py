#레벨2.다리를 지나는 트럭
#https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

from collections import deque
def solution(bridge_length, weight, truck_weights):
    dq = deque()
    answer = 1
    idx = 1
    now= truck_weights[0]
    dq.append([truck_weights[0],0])
    while dq :
        for i in dq:
            i[1] += 1
        while dq:
            if dq[0][1] < bridge_length:
                break
            now-= dq.popleft()[0]
        if idx<len(truck_weights):
            if now + truck_weights[idx] <= weight and len(dq)+1<=bridge_length:
                dq.append([truck_weights[idx], 0])
                now += truck_weights[idx]
                idx += 1
        answer+=1
    return answer