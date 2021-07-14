#레벨1.약수의 개수와 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer=0
    for i in range(left,right+1) :
        if int(i**0.5) == i**0.5 :
            answer-=i
        else :
            answer+=i 
    
    return answer