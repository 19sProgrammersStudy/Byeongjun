#레벨2.최댓값과 최솟값
#https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3

def solution(s):
    lst=list(map(int,s.split(' ')))
    answer = str(min(lst))+" "+str(max(lst))
    return answer