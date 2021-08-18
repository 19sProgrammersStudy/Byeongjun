#레벨2.문자열 압축
#https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    if len(s)==1 : return 1
    round=len(s)//2
    min=1001
    for i in range(round,0,-1) :
        #temp=list(map(''.join, zip(*[iter(s)]*round)))
        temp,templi=s,[]
        while len(temp)>0 :
            if i<=len(temp):
                templi.append(temp[:i])
                temp=temp[i:]
            else :
                templi.append(temp)
                temp=""
        count,idx=1,0
        string=""
        while idx<len(templi)-1 :
            if idx==len(templi)-2 :
                if templi[idx+1]==templi[idx] :
                    count+=1
                    string = string + str(count) + templi[idx]
                else :
                    if count!=1 : string=string+str(count)+templi[idx]+templi[idx+1]
                    else: string=string+templi[idx]+templi[idx+1]
                    count=1
                idx+=1
            else :
                if templi[idx+1]==templi[idx] :
                    count+=1
                else :
                    if count!=1 : string=string+str(count)+templi[idx]
                    else: string=string+templi[idx]
                    count=1
                idx+=1
        if min > len(string) : min = len(string)
    return min