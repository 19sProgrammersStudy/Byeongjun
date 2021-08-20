#레벨2.수식 최대화
#https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3

from itertools import permutations as per
def solution(expression):
    answer = 0
    startidx,endidx=0,0
    susik,ex=[],[]
    for i in ["-","+","*"]:
        if i in expression : susik.append(i)
    susik=list(per(susik,len(susik)))
    while endidx<len(expression):
        if expression[endidx]=="-" or expression[endidx]=="+" or expression[endidx]=="*":
            ex.append(expression[startidx:endidx])
            ex.append(expression[endidx])
            startidx,endidx=endidx+1,endidx+1
        if endidx==len(expression)-1 :
            ex.append(expression[startidx:endidx+1])
        endidx+=1
    for i in range(len(susik)) :
        temp,tot=ex[:],0
        for j in range(len(susik[i])) :
            while susik[i][j] in temp :
                if susik[i][j]=='-' :
                    idx=temp.index(susik[i][j])
                    now =int(temp[idx-1]) - int(temp[idx+1])
                    del temp[idx-1]
                    del temp[idx-1]
                    temp[idx-1]=str(now)
                elif susik[i][j]=='+' :
                    idx = temp.index(susik[i][j])
                    now = int(temp[idx - 1]) + int(temp[idx + 1])
                    del temp[idx - 1]
                    del temp[idx - 1]
                    temp[idx - 1] = str(now)
                elif susik[i][j]=='*' :
                    idx = temp.index(susik[i][j])
                    now = int(temp[idx - 1]) * int(temp[idx + 1])
                    del temp[idx - 1]
                    del temp[idx - 1]
                    temp[idx - 1] = str(now)
        if abs(int(temp[0]))>answer : answer=abs(int(temp[0]))
    return answer
