#레벨 1. 신규 아이디 추천
#https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(new_id):
    #1단계
    new_id=new_id.lower()
    #2단계
    temp=""
    for i in range(len(new_id)) :
        if (48<=int(ord(new_id[i]))<=57) or (97<=int(ord(new_id[i]))<=122) or (45<=int(ord(new_id[i]))<=46) or int(ord(new_id[i]))==95 :
            temp+=new_id[i]
    new_id=temp
    #3단계
    while new_id.count("..")!=0 :
        new_id=new_id.replace('..','.')
    #4단계
    if new_id[0] == '.' :new_id= new_id[1:] if len(new_id)>1 else '.'
    if new_id[-1] == '.' : new_id=new_id[:-1]
    #5단계
    if len(new_id)==0 : new_id="a"
    #6단계
    if len(new_id) >15 :
        new_id=new_id[:15]
        if new_id[-1]=='.' : new_id=new_id[:-1]
    #7단계
    while len(new_id) <3 :
        new_id=new_id+new_id[-1]
    answer=new_id
    return answer