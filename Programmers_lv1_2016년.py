#레벨 1. 2016년
#https://programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    day=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    tot=0
    for i in range(1,a) :
        if i in [1,3,5,7,8,10,12] :
            tot+=31
        elif i in [4,6,9,11] :
            tot+=30
        else : tot+=29
    tot+=b
    n = tot%7-1
    answer = day[n]
    return answer