#레벨2.영어 끝말잇기
#https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3

def solution(n, words):
    people=list(range(1,n+1))
    answer,use=[],[]
    before,idx,round="",0,1
    while True:
        for i in people :
            if idx==len(words) :
                answer=[0,0]
                return answer
            if (words[idx] in use or before!=words[idx][0]) and idx!=0:
                answer=[i,round]
                return answer
            use.append(words[idx])
            before=words[idx][-1]
            idx+=1
        round+=1
    return answer