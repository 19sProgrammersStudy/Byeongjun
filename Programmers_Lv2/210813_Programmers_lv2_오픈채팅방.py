# 레벨2.오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

"""def solution(record):
    lst=[[],[]]
    nick=[[],[]]
    answer = []
    for i in record :
        temp=list(i.split(" "))
        if temp[0]=="Enter" :
            lst[0].append(temp[1])
            lst[1].append("님이 들어왔습니다.")
            if temp[1] in nick[0] :
                nick[1][nick[0].index(temp[1])]=temp[2]
            else :
                nick[0].append(temp[1])
                nick[1].append(temp[2])
        elif temp[0]=="Leave" :
            lst[0].append(temp[1])
            lst[1].append("님이 나갔습니다.")
        elif temp[0]=="Change" :
            for j in range(len(nick[0])) :
                if nick[0][j]==temp[1] :
                    nick[1][j]=temp[2]
    #print(lst)
    #print(nick)
    for i in range(len(lst[0])):
        idx=nick[0].index(lst[0][i])
        answer.append(nick[1][idx]+lst[1][i])

    return answer"""


def solution(record):
    nick = {}
    answer = []
    for i in record:
        if i.split(" ")[0] == "Enter" or i.split(" ")[0] == "Change":
            nick[i.split(" ")[1]] = i.split(" ")[2]
    for i in record:
        if i.split(" ")[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(nick[i.split(" ")[1]]))
        elif i.split(" ")[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(nick[i.split(" ")[1]]))
    return answer