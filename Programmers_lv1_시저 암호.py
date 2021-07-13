#레벨 1. 시저 암호
#https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3

def solution(s, n):
    answer = ""
    for i in s :
        if 65<=int(ord(i))<=90 :
            if int(ord(i))+n > 90 :
                answer+=chr(int(ord(i))+n-26)
            else :
                answer+=chr(int(ord(i))+n)
        elif 97<=int(ord(i))<=122  :
            if int(ord(i))+n > 122 :
                answer+=chr(int(ord(i))+n-26)
            else :
                answer+=chr(int(ord(i))+n)
        else : answer+=i
    return answer