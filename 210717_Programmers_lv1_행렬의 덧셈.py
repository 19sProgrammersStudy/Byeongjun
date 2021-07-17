#레벨1.행렬의 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3

def solution(arr1, arr2):
    answer=arr1
    for i in range(len(arr1)) :
        for j in range(len(arr1[i])):
            answer[i][j]=arr1[i][j]+arr2[i][j]
    return answer