#레벨2.방문 길이
#https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3

def solution(dirs):
    answer = 0
    move=[]
    nx,ny=5,5
    lst=[[0]*11 for _ in range(11)]
    for i in dirs :
        dx,dy=nx,ny
        if i=="U" : dy-=1
        elif i=="D" : dy+=1
        elif i=="L" : dx-=1
        else : dx+=1
        if 0<=dx<11 and 0<=dy<11 :
            temp=[[nx,ny,dx,dy],[dx,dy,nx,ny]]
            flag=True
            for j in temp :
                if j in move : flag=False
            if flag==True :
                print(temp[0])
                move.append(temp[0])
                answer+=1
            nx,ny=dx,dy
    return answer