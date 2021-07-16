#레벨1.자릿수 더하기
#https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3

def solution(n):
    answer = 0
    n=str(n)
    lst=list(n)
    for i in lst : 
        answer+=int(i)
    return answer