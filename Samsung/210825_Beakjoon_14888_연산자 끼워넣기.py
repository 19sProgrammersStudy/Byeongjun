#Beakjoon_14888_연산자 끼워넣기
#https://www.acmicpc.net/problem/14888

def check(operator) :
    for i in range(len(operator)) :
        if operator[i]!=0 : return False
    return True
def dfs(num,operator) :
    global max_num,min_num
    if check(operator)  :
        if num[0]>max_num : max_num=num[0]
        if num[0]<min_num : min_num=num[0]
        return
    for i in range(4) :
        if operator[i]!=0 :
            num_lst=num[:]
            operator[i]=operator[i]-1
            if i== 0 :
                temp= num_lst[0]+num_lst[1]
                del num_lst[0]
                del num_lst[0]
                num_lst.insert(0,temp)
                dfs(num_lst,operator)
            elif i == 1:
                temp = num_lst[0] - num_lst[1]
                del num_lst[0]
                del num_lst[0]
                num_lst.insert(0, temp)
                dfs(num_lst, operator)
            elif i==2 :
                temp = num_lst[0] * num_lst[1]
                del num_lst[0]
                del num_lst[0]
                num_lst.insert(0, temp)
                dfs(num_lst, operator)
            else :
                if num_lst[0]<0 and num_lst[1]>0 :
                    temp = -(num_lst[0]) // num_lst[1]
                    del num_lst[0]
                    del num_lst[0]
                    num_lst.insert(0, -temp)
                    dfs(num_lst, operator)
                else :
                    temp = num_lst[0] // num_lst[1]
                    del num_lst[0]
                    del num_lst[0]
                    num_lst.insert(0, temp)
                    dfs(num_lst, operator)
            operator[i] = operator[i] + 1
max_num,min_num=-1000000000,1000000000
n=int(input())
lst=list(map(int,input().split()))
operator=list(map(int,input().split()))

dfs(lst,operator)

print(max_num,min_num)