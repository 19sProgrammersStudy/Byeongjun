#레벨1.문자열 내림차순으로 배치하기
#https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3

def solution(s):
    temp=[]
    answer = ""
    for i in s : 
        temp.append(ord(i))
    temp.sort(reverse=True)
    for i in temp :
        answer+=chr(i)
    return answer