#레벨1.두 개 뽑아서 더하기
#https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

from itertools import combinations as cb
def solution(numbers):
    answer = []
    for i in cb(numbers,2):
        temp= i[0]+i[1]
        if temp not in answer :
            answer.append(temp)
    answer.sort()
    return answer
