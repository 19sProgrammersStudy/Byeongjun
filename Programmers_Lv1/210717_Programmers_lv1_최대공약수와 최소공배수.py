#레벨1.최대공약수와 최소공배수
#https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3

def solution(n, m):
    answer = []
    #최대공약수 구하기 
    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i==0 : 
            answer.append(i)
            break
    #최소공배수 구하기
    for i in range(1,min(n,m)+1):
        idx=1
        while min(n,m)*idx<=max(n,m)*i:
            if  min(n,m)*idx==max(n,m)*i :
                answer.append(max(n,m)*i)
                return answer
            idx+=1
    return answer