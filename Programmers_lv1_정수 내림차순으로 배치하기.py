#레벨1.정수 내림차순으로 배치하기
#https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3

def solution(n):
    lst=list(str(n))
    answer=""
    for i in range(len(lst)) : 
        lst[i]=int(lst[i])
    lst.sort(reverse=True)
    for i in range(len(lst)) : 
        answer+=str(lst[i])
    answer=int(answer)
    return answer