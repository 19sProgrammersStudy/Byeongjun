#레벨1.문자열 내 마음대로 정렬하기
#https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3

def solution(strings, n):
    for i in range(len(strings)):
        strings[i]=strings[i][n]+strings[i]
    strings.sort()
    answer=[]
    for i in range(len(strings)):
        answer.append(strings[i][1:])
    return answer