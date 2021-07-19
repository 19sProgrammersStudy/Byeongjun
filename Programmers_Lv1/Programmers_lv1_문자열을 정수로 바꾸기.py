#레벨1.문자열을 정수로 바꾸기
#https://programmers.co.kr/learn/courses/30/lessons/12925?language=python3

def solution(s):
    if s[0]=='+': 
        answer=int(s[1:])
    elif s[0]=='-':
        answer=-int(s[1:])
    else : answer=int(s)
    return answer