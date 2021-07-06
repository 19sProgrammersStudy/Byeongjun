def solution(lottos, win_nums):
    answer = [0, 0]
    count1 = 0
    count2 = 0
    answer1 = 0
    answer2 = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            count1 += 1
            count2 += 1
        if i == 0: zero += 1

    for j in range(1, 45):
        if zero == 0: break;
        if j in win_nums and j not in lottos:
            count1 += 1
            zero -= 1
    print(count1, count2)
    if count1 == 6:
        answer[0] = 1
    elif count1 == 5:
        answer[0] = 2
    elif count1 == 4:
        answer[0] = 3
    elif count1 == 3:
        answer[0] = 4
    elif count1 == 2:
        answer[0] = 5
    else:
        answer[0] = 6

    if count2 == 6:
        answer[1] = 1
    elif count2 == 5:
        answer[1] = 2
    elif count2 == 4:
        answer[1] = 3
    elif count2 == 3:
        answer[1] = 4
    elif count2 == 2:
        answer[1] = 5
    else:
        answer[1] = 6

    return answer