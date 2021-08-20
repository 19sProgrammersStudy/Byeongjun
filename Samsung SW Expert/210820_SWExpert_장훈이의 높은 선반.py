#SWExpert 1486. 장훈이의 높은 선반
#https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

def dfs(idx,now) :
    global b,mininum,employee
    if now>=b:
        if abs(b-now)<mininum :
            mininum=abs(b-now)
            return
    for i in range(idx,len(employee)) :
        dfs(i+1,now+employee[i])

t=int(input())
for i in range(1,t+1) :
    n,b=map(int,input().split(" "))
    employee=list(map(int,input().split(" ")))
    mininum=sum(employee)
    for j in range(len(employee)) :
        now=employee[j]
        dfs(j+1,now)
    print("#{} {}".format(i,mininum))