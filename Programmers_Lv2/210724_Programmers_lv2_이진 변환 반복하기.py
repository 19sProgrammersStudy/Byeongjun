#레벨2.이진 변환 반복하기
#https://programmers.co.kr/learn/courses/30/lessons/70129?language=python3

def calculate(now) :
    next=""
    while now>0 : 
        next=str(now%2)+next
        now=now//2
    return next

def solution(s):
    cnt=0
    zero=0
    while s!='1' :
        temp = ""
        for i in s :
            if i == '1' : temp+=i
            else : zero+=1
        s=calculate(len(temp))
        cnt+=1
    answer = [cnt,zero]
    return answer