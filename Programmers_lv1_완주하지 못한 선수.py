#레벨1. 완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)) : 
        if participant[i]!= completion[i] :
            answer=participant[i]
            return answer
        elif i==len(completion)-1 : 
            answer=participant[i+1]
            return answer