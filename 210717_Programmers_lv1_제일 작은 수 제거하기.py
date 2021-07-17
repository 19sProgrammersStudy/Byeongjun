#레벨1.제일 작은 수 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3

def solution(arr):
    del arr[arr.index(min(arr))]
    if len(arr)==0 : 
        answer=[-1]
    else :      
        answer = arr
    
    return answer