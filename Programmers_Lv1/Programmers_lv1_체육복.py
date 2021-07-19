#레벨1. 체육복
#https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
def solution(n, lost, reserve):
    answer = 0
    lst = []
    for i in range(n) :
        if (i+1 in lost and i+1 in reserve) or (i+1 not in lost and i+1 not in reserve) :
            lst.append(1)
        elif i+1 in lost and i+1 not in reserve :
            lst.append(0)
        elif i+1 not in lost and i+1 in reserve : 
            lst.append(2)
    
    for i in range(len(lst)) : 
        if i==0 and lst[i]==0 and lst[i+1]==2 : 
            lst[i]+=1
            lst[i+1]-=1
        elif 0<i<len(lst)-1 and lst[i]==0 :
            if lst[i-1]>1 : 
                lst[i]+=1
                lst[i-1]-=1
            elif lst[i+1]>1 :
                lst[i]+=1
                lst[i+1]-=1
        elif i==len(lst)-1 and lst[i]==0 and lst[i-1]==2 :
            lst[i]+=1
            lst[i-1]-=1
    answer = len(lst) - lst.count(0)
    return answer