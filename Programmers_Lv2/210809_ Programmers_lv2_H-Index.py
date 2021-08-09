#레벨2.H-Index
#https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):
    n=len(citations)
    mx=max(citations)
    cnt=0
    answer = 0
    for i in range(mx,-1,-1) :
        cnt=cnt+citations.count(i)
        if cnt>=i :
            answer=i
            break
    return answer