#레벨1. 예산
#https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d :
        if budget>=i : 
            answer+=1
            budget -=i
    
    return answer