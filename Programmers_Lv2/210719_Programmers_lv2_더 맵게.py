#레벨 2.더 맵게
#https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K : 
        mix=heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville,mix)
        answer+=1
        if len(scoville)==1 and  scoville[0]<K :
            return -1
    return answer

   # 일반적인 소팅으로 문제를 풀 경우 시간초과 발생
   # while min(scoville)<K : 
   #     if scoville.count(0)==len(scoville) or len(scoville)==0:
    #        return -1
     #   scoville.sort()
      #  scoville.append(scoville[0]+(scoville[1]*2))
       # for i in range(2):
        #    del scoville[0]
        #answer+=1