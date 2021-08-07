#레벨2.위장
#https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

def solution(clothes):
    kind=[]
    combo=[]
    answer = 1
    for i in clothes :
        if i[1] not in kind :
            kind.append(i[1])
    for i in kind :
        combo.append([i])
    for i in clothes :
        idx=kind.index(i[1])
        combo[idx].append(i[0])
    for i in range(len(combo)):
        answer*=len(combo[i])
    return answer-1