#Beakjoon_13458_시험 감독
#https://www.acmicpc.net/problem/13458

n=int(input())
test_room=list(map(int,input().split()))
b,c=map(int,input().split())
answer=n
for i in range(len(test_room)) :
    #정담당자 배치
    if test_room[i]-b < 0 : test_room[i]=0
    else : test_room[i]-=b
    #부담당자 배치
    if test_room[i] :
        answer+= test_room[i]//c
        if test_room[i]%c !=0 : answer+=1

print(answer)