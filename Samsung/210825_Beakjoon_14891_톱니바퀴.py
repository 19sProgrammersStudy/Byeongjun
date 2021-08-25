#Beakjoon_14891_톱니바퀴
#https://www.acmicpc.net/problem/14891

#회전 함수
def rotate(num,dir) :
    global gear
    lst=gear[num]
    if dir==-1 :
        temp=lst[0]
        lst=lst[1:]
        lst.append(temp)
        return lst
    else :
        temp = lst[-1]
        lst = lst[:-1]
        lst.insert(0,temp)
        return lst

gear=[]
for i in range(4) :
    temp=[]
    for j in str(input()) :
        temp.append(int(j))
    gear.append(temp)
k=int(input())
for i in range(k) :
    roll=gear[:]
    num,dir=map(int,input().split())
    num-=1
    roll[num]=rotate(num,dir)
    dirleft,dirright=dir,dir
    for j in range(num,0,-1) :
        if gear[j][6] == gear[j-1][2] :
            break;
        dirleft=-dirleft
        roll[j-1]=rotate(j-1,dirleft)
    for k in range(num,len(roll)-1) :
        if gear[k][2] == gear[k+1][6] :
            break
        dirright=-dirright
        roll[k+1]=rotate(k+1,dirright)
    gear=roll[:]
total,plus=0,1
for i in range(4) :
    if gear[i][0]==1 :
        total+=plus
    plus*=2
print(total)
