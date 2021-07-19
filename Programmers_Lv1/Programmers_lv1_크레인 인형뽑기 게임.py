#레벨1. 크레인 인형뽑기 게임
#https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
from collections import deque
def solution(board, moves):
    answer = 0
    dq = deque()
    for i in moves :
        for j in range(len(board[i-1])) : 
            if board[j][i-1]!=0 : 
                dq.appendleft(board[j][i-1])
                board[j][i-1]=0
                if len(dq)>1 and dq[0]==dq[1] : 
                    dq.popleft()
                    dq.popleft()
                    answer+=2
                break     
    return answer