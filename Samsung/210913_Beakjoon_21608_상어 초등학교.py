#Beakjoon_21608_상어 초등학교
#https://www.acmicpc.net/problem/21608

n=int(input())
student=[]
ind=[]
dx,dy=[-1,0,1,0],[0,1,0,-1]
classroom=[[0]*n for _ in range(n)]
for i in range(n**2):
    num,o,t,th,f=map(int,input().split())
    student.append([num,o,t,th,f])
    ind.append(num)

flag=True
#첫번째 기준잡기
for j in range(n):
    for k in range(n):
        count=0
        for l in range(4):
            nx,ny=j+dx[l],k+dy[l]
            if 0<=nx<n and 0<=ny<n :
                count+=1
        if count==4 :
            classroom[j][k]=student[0][0]
            flag=False
            break
    if flag==False : break

for t in range(1,n**2):
    candidate=[]
    for i in range(n):
        for j in range(n):
            like_count=0
            empty=0
            if classroom[i][j]==0 :
                for k in range(4):
                    nx,ny=i+dx[k],j+dy[k]
                    if 0<=nx<n and 0<=ny<n :
                        if classroom[nx][ny] in student[t][1:] :
                            like_count+=1
                        if classroom[nx][ny]==0 :
                            empty-=1
                if not candidate :
                    candidate.append([like_count, empty, i, j])
                elif candidate[0][0]==like_count :
                    candidate.append([like_count,empty,i,j])
                elif candidate[0][0]<like_count :
                    candidate.clear()
                    candidate.append([like_count,empty,i,j])
    candidate.sort()
    classroom[candidate[0][2]][candidate[0][3]]=student[t][0]
answer=0
for i in range(n) :
    for j in range(n):
        idx=ind.index(classroom[i][j])
        count=0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if classroom[nx][ny] in student[idx][1:] :
                    count+=1
        if count==1 : answer+=1
        elif count==2 : answer+=10
        elif count==3 : answer+=100
        elif count==4 : answer+=1000

print(answer)



