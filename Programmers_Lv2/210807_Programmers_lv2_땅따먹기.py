#레벨2.땅따먹기
#https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3

def solution(land):
    for i in range(len(land)-1):
        land[i+1][0]+=max(land[i][1],land[i][2],land[i][3])
        land[i+1][1]+=max(land[i][0],land[i][2],land[i][3])
        land[i+1][2]+=max(land[i][0],land[i][1],land[i][3])
        land[i+1][3]+=max(land[i][0],land[i][1],land[i][2])
    answer=max(land[len(land)-1])

    return answer