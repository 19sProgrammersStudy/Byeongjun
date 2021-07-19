#레벨1.자연수 뒤집어 배열로 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3

def solution(n):
    answer=list(str(n))
    for i in range(len(answer)) : 
        answer[i]=int(answer[i])
    answer.reverse()
    return answer