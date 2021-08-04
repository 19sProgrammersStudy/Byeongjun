#레벨2.가장 큰 정사각형 찾기
#https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3

"""
def solution(board):
    answer = 0
    now = min(len(board),len(board[0]))
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    while now>1 :
        for i in range(now-1,len(board[0])) :
            for j in range(now-1,len(board)) :
                flag=True
                for k in range(j-now+1,j+1) :
                    temp=board[k][i-now+1:i+1]
                    if 0 in temp :
                        flag= False
                        break
                if flag==True :
                    answer=now*now
                    return answer
        now-=1
    for i in range(len(board)) :
        if 1 in board[i] : return 1
    return 0
"""
def solution(board):
    dp=[[0]*len(board[0]) for _ in range(len(board))]
    dp[0]=board[0]
    for i in range(1,len(board)) :
        dp[i][0]=board[i][0]

    for i in range(1,len(board)) :
        for j in range(1,len(board[0])) :
            if board[i][j]==1 :
                dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
    answer = 0
    for i in range(len(board)):
        temp=max(dp[i])
        answer=max(answer,temp)
    return answer*answer
