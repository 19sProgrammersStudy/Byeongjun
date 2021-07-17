#레벨1.소수 찾기
#https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3

def solution(n):
    answer=0
    lst =[1]*(n+1)
    lst[0],lst[1]=0,0
    for i in range(2,n+1):
        if lst[i] :
            answer+=1
            idx=2
            while i*idx<=n:
                lst[i*idx]=0
                idx+=1
    return answer