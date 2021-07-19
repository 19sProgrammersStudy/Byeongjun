#레벨1.핸드폰 번호 가리기
#https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3

def solution(phone_number):
    answer = ''
    answer+="*"*(len(phone_number)-4)
    answer+=phone_number[len(phone_number)-4:]
    return answer