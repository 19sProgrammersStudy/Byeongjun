#레벨2.점프와 순간 이동
#https://programmers.co.kr/learn/courses/30/lessons/12980?language=python3

def solution(n):
    ans = 0
    while n>0 :
        if n%2 !=0 :
            n-=1
            ans+=1
        n//=2
    return ans