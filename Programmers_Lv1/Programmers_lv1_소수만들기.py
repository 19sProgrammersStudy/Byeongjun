from itertools import combinations as cb
def solution(nums):
    answer = 0
    for i in cb(nums, 3):
        flag=False;
        li_sum=sum(i)
        for j in range(2,li_sum):
            if li_sum%j==0 :
                flag=True
                break;
        if flag == False :
            answer+=1
    return answer