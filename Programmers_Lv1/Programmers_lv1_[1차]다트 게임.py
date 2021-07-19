#레벨1. [1차]다트 게임
#https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3

def solution(dartResult):
    answer = 0
    score= []
    idx=-1
    num=""
    for i in dartResult :
        if i.isdigit() :
            num+=i
        else :
            if num!="" :
                score.append(int(num))
                idx+=1
                num=""
            if i.isalpha() :
                if i=='S':  score[idx]=score[idx]**1
                elif i=='D': score[idx]=score[idx]**2
                elif i=='T': score[idx]=score[idx]**3
            else :
                if i=='*' :
                    if idx==0 : score[idx]*=2
                    else :
                        score[idx]*=2
                        score[idx-1]*=2
                else :
                    score[idx]*=-1
    for i in score :
        answer+=i
    return answer