#레벨2.예상 대진표
#https://programmers.co.kr/learn/courses/30/lessons/12985?language=python3

def solution(n,a,b):
    answer = 0
    while True : 
        if a==b : break
        if a%2 ==1 : a=(a//2)+1
        else : a=a//2
        if b%2 ==1 : b=(b//2)+1
        else : b=b//2
        answer+=1
    return answer