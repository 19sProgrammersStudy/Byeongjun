#레벨 1. 숫자 문자열과 영단어
#https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ""
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    flag = 0
    temp = ""
    while flag < len(s):
        if 97 <= ord(s[flag]) <= 122:
            temp += s[flag]
            if temp in number :
                answer+=str(int(number.index(temp)))
                temp = ""
        else:
            answer+=str(s[flag])
        flag += 1
    return int(answer)