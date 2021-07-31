def solution(brown, yellow):
    temp = (brown//2)-2
    answer = []
    for ver in range(1,temp):
        hor= temp-ver
        total = (ver+2)*(hor+2)
        if total-brown == yellow :
            answer=[hor+2,ver+2]
            return answer
    return answer