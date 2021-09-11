#Beakjoon_14499_주사위 굴리기
#https://www.acmicpc.net/problem/14499

def turn(dir):
    global dice
    if dir==1 :
        one,two,three,four,five,six=dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]
    elif dir==2 :
        one, two, three, four, five, six = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif dir == 3:
        one, two, three, four, five, six = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    else :
        one, two, three, four, five, six = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
    return [one,two,three,four,five,six]

n,m,x,y,k=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
dice=[0,0,0,0,0,0]
dx,dy=[0,0,-1,1],[1,-1,0,0]
for i in map(int,input().split()):
    nx,ny=x+dx[i-1],y+dy[i-1]
    if 0<=nx<n and 0<=ny<m :
        dice=turn(i)
        if board[nx][ny]==0 : board[nx][ny]=dice[5]
        else :
            dice[5]=board[nx][ny]
            board[nx][ny]=0
        print(dice[0])
        x,y=nx,ny
