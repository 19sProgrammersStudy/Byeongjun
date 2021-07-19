#레벨1.키패드 누르기
#https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    leftnow="*"
    rightnow="#"
    leftlst=["1","4","7","*"]
    centerlst=["2","5","8","0"]
    rightlst=["3","6","9","#"]
    answer=""
    for i in numbers :
        if str(i) in leftlst :
            answer+="L"
            leftnow=str(i)
        elif str(i) in rightlst :
            answer+="R"
            rightnow=str(i)
        else :
            if leftnow in leftlst :
                lnum=abs(leftlst.index(leftnow)-centerlst.index(str(i)))+1
            else : lnum=abs(centerlst.index(leftnow)-centerlst.index(str(i)))
            if rightnow in rightlst :
                rnum=abs(rightlst.index(rightnow)-centerlst.index(str(i)))+1
            else : rnum=abs(centerlst.index(rightnow)-centerlst.index(str(i)))
            if lnum<rnum :
                answer+="L"
                leftnow=str(i)
            elif lnum>rnum :
                answer+="R"
                rightnow=str(i)
            else :
                if hand=="left" :
                    answer+="L"
                    leftnow=str(i)
                else :
                    answer+="R"
                    rightnow=str(i)
    return answer