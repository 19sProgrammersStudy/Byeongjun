#Beakjoon_17143_낚시왕
#https://www.acmicpc.net/problem/17143

from collections import deque
r,c,m=map(int,input().split())
board=[[deque() for _ in range(c)] for _ in range(r)]
answer=0
for i in range(m):
    x,y,s,d,z=map(int,input().split())
    board[x-1][y-1].append([s,d,z])
for i in range(c):
    #상어잡이
    for j in range(r):
        if board[j][i] :
            s,d,z=board[j][i].popleft()
            answer+=z
            break
    #상어이동
    board_copy=[[deque() for _ in range(c)] for _ in range(r)]
    for j in range(r):
        for k in range(c):
            if board[j][k] :
                s, d, z = board[j][k].popleft()
                if d<=2 :length=s%((r-1)*2)
                else : length=s%((c-1)*2)
                now_x,now_y=j,k
                while length :
                    if d==1 :
                        if length<now_x-0 :
                            now_x-=length
                            length=0
                        else :
                            length-=now_x-0
                            now_x=0
                            d=2
                    elif d==2 :
                        if length<r-1-now_x :
                            now_x+=length
                            length=0
                        else :
                            length-=r-1-now_x
                            now_x=r-1
                            d=1
                    elif d == 3:
                        if length < c-1-now_y:
                            now_y += length
                            length = 0
                        else:
                            length -= c-1-now_y
                            now_y = c-1
                            d = 4
                    elif d == 4:
                        if length < now_y - 0:
                            now_y -= length
                            length = 0
                        else:
                            length -= now_y-0
                            now_y = 0
                            d = 3
                if board_copy[now_x][now_y] :
                    if board_copy[now_x][now_y][0][2] < z :
                        board_copy[now_x][now_y].popleft()
                        board_copy[now_x][now_y].append([s,d,z])
                else :
                    board_copy[now_x][now_y].append([s, d, z])
    board=board_copy[:]

print(answer)