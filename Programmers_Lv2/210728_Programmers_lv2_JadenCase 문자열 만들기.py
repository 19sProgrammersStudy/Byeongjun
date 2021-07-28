#레벨2.JadenCase 문자열 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3

def solution(s):
    lst=list(s)
    idx=False
    answer=""
    for i in range(len(s)) : 
        if lst[i]!=" " and idx== False: 
            lst[i]=lst[i].upper()
            idx=True
        elif lst[i]!=" " and idx==True : 
            lst[i]=lst[i].lower()
        elif lst[i]== " ":
            idx=False
    for i in lst : 
        answer+=i
    return answer 