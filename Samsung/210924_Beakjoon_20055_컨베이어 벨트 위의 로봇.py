n,k=map(int,input().split())
lst=list(map(int,input().split()))
robot=[0]*(2*n)
round=0
while lst.count(0)<k :
    #컨베이어 회전
    temp=lst[-1]
    lst[1:] = lst[:-1]
    lst[0]=temp
    #로봇 위치 회전
    temp=robot[-1]
    robot[1:]=robot[:-1]
    robot[0]=temp
    if robot[n-1] :
        robot[n-1]=0
    #로봇 이동
    for i in range(n-1,0,-1):
        if robot[i-1]==1 and robot[i]==0 and lst[i]!=0 :
            robot[i-1]=0
            robot[i]=1
            lst[i]-=1
    if robot[n-1] :
        robot[n-1]=0
    #로봇 올리기
    if lst[0]!=0 :
        robot[0]=1
        lst[0]-=1
    round+=1
print(round)