#레벨2.[1차]뉴스 클러스터링
#https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3

def solution(str1, str2):
    answer = 0
    #str1,str2 초기화
    li1,li2=[],[]
    for i in range(len(str1)-1) :
        temp=str1[i]+str1[i+1]
        if temp.isalpha() :
            li1.append(temp.lower())
    for i in range(len(str2)-1) :
        temp=str2[i]+str2[i+1]
        if temp.isalpha() :
            li2.append(temp.lower())
    same=0
    #교집합 갯수 구하기 위해 large(길이가 긴 배열), small(길이가 짧은 배열) 선언
    if len(li1)>=len(li2) : large,small=li1[:],li2[:]
    else : large,small=li2[:],li1[:]
    #짧은 배열 For문 돌려서 긴 배열에 있으면 +1 and 긴 배열에서 제거
    for i in small :
        if i in large :
            same+=1
            large.remove(i)
    total = len(li1)+len(li2)-same
    #공집합일 경우 65536 리턴
    if same==total==0 :  return 65536
    answer=int((same/total)*65536)
    return answer