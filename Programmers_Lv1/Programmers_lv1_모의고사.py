#레벨 1. 모의고사
#https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    idx1, idx2, idx3 = 0, 0, 0
    count = [0, 0, 0]

    for i in answers:
        if i == student1[idx1]:
            count[0] += 1
        if i == student2[idx2]:
            count[1] += 1
        if i == student3[idx3]:
            count[2] += 1
        if idx1 + 1 == len(student1):
            idx1 = 0
        else:
            idx1 += 1
        if idx2 + 1 == len(student2):
            idx2 = 0
        else:
            idx2 += 1
        if idx3 + 1 == len(student3):
            idx3 = 0
        else:
            idx3 += 1
    maxnum = max(count)
    for i in range(len(count)):
        if count[i] == maxnum:
            answer.append(i + 1)
    return answer

