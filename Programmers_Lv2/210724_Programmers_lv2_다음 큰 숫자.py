#레벨2.다음 큰 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3

def calculate(num) :
    cnt=0 
    while num!=0 : 
        if num%2 == 1 : cnt+=1
        num=num//2
    return cnt

def solution(n):
    answer = 0
    cnt= calculate(n) 
    for i in range(n+1,1000001) : 
        if cnt == calculate(i) :
            answer=i
            break
    return answer