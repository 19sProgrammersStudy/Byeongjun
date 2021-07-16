#레벨1.수박수박수박수박수박수?
#https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3

def solution(n):
    answer = ''
    for i in range(n//2):
        answer+="수박"
    if n%2!=0 : answer+="수"  
    return answer