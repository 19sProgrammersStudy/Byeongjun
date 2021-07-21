#레벨2.기능개발
#https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

from collections import deque 
def solution(progresses, speeds):
    dq=deque(progresses)
    answer = []
    while dq :
        if dq[0]>=100 :
            count=0 
            while dq : 
                if dq[0]<100 : 
                    break
                dq.popleft()
                del speeds[0]
                count+=1
            answer.append(count)
        for i in range(len(dq)) : 
            dq[i]+=speeds[i]
    return answer