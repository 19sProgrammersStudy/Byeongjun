#레벨1. 콜라츠 추측
#https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    cnt = 0
    while cnt < 500:
        if num == 1:
            answer = cnt
            return answer

        if num % 2 == 0:
            num /= 2
        elif num % 2 != 0:
            num = num * 3 + 1
        cnt += 1
    return -1