#레벨1.약수의 합
#https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3

def solution(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0 : 
            if i not in lst :lst.append(i) 
            if n//i not in lst : lst.append(n//i)
    answer = sum(lst)
    return answer