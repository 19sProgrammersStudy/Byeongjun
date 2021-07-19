#레벨1.하샤드 수 
#https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3

def solution(x):
    answer = False
    x=str(x)
    lst=list(x)
    x=int(x)
    num=0
    for i in lst : 
        num+=int(i)
    if x%num ==0 :
        answer = True
    return answer