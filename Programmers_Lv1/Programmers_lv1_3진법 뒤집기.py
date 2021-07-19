#레벨1. 3진법 뒤집기
#https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3

def solution(n):
    tri=""
    answer=0
    while n!=0 : 
        tri+=str(n%3)
        n=n//3
    n=1
    for i in range(len(tri)-1,-1,-1) :
        answer+= int(tri[i])*n
        n*=3
    return answer