def solution(N, stages):
    fail = []
    answer = []
    for i in range(N):
        stay = 0
        arrive = 0
        failure = 0
        for j in stages:
            if j >= i + 1: arrive += 1
            if j == i + 1: stay += 1
        if stay != 0 and arrive != 0:
            failure = stay / arrive
        fail.append(failure)
    for i in range(N):
        idx = fail.index(max(fail))
        answer.append(idx + 1)
        fail[idx] = -1

    return answer

 #https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3