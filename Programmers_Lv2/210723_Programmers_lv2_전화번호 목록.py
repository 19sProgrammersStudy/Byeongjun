#레벨2.전화번호 목록
#https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i])<=len(phone_book[i+1]) :
            if phone_book[i]==phone_book[i+1][:len(phone_book[i])] :
                    return False
    return answer

#다른풀이
#def solution(phoneBook):
#    phoneBook = sorted(phoneBook)
#
#    for p1, p2 in zip(phoneBook, phoneBook[1:]):
#        if p2.startswith(p1):
#            return False
#    return True