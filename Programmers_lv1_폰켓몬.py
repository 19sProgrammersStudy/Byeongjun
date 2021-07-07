def solution(nums):
    li = []
    answer = 0
    for i in nums:
        if i not in li:
            li.append(i)
    sel = len(nums) // 2
    if sel <= len(li):
        answer = sel
    else:
        answer = len(li)
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/1845