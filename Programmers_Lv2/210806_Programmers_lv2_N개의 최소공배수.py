#레벨2.N개의 최소공배수
#https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3

def solution(arr):
    while len(arr)>1 :
        arr.sort()
        for i in range(1,arr[1]+1) :
            if arr[0]*i % arr[1] == 0 :
                arr.append(arr[0]*i)
                arr=arr[2:]
                break
    answer=arr[0]
    return answer