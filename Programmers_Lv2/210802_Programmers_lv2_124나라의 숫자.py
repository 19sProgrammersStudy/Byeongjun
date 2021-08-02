# 레벨2.124나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3

def solution(n):
    num = ["1", "2", "4"]
    answer = ""
    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
    return answer
