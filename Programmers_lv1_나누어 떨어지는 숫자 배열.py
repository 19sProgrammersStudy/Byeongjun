#레벨1.나누어 떨어지는 숫자 배열
#https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor==0 : 
            answer.append(i)
    answer.sort()
    if len(answer)==0 :
        answer.append(-1)
    return answer