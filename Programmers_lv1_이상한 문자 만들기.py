#레벨1.이상한 문자 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

def solution(s):
    answer = ""
    idx=0
    for i in range(len(s)) :
        if s[i].isalpha() :
            if idx%2!=0 : 
                answer+=s[i].lower()
            else : answer+=s[i].upper()
                
            idx+=1
        else :
            answer+=" "
            idx=0
    return answer