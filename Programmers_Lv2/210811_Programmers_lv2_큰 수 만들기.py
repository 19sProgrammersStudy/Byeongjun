#레벨2.큰 수 만들기
#https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

def solution(number, k):
    stack=[]
    for i in range(len(number)):
        while stack and stack[-1]<number[i] and k>0 :
            stack.pop()
            k-=1
        stack.append(number[i])
    if k>0 :
        stack=stack[:-k]
    answer="".join(stack)
    return answer