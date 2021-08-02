#레벨2.스킬트리
#https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3

def solution(skill, skill_trees):
    answer=0
    for i in range(len(skill_trees)) :
        flag=True
        past=[]
        for j in skill_trees[i] :
            if j in skill :
                past.append(j)
        for j in range(len(past)) :
            if past[j]!=skill[j] :
                flag=False
                break
        if flag==True :
            answer+=1
    return answer