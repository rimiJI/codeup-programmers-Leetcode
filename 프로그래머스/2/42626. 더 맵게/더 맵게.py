import heapq as h

def solution(scoville, K):
    h.heapify(scoville) #힙자료형으로
    count=0
    
    while scoville[0]<K:
        count+=1
        min1=h.heappop(scoville) #heappop 가장 작은 값 제거후 반환 
        min2=h.heappop(scoville)
        h.heappush(scoville,min1+min2*2)
        if (len(scoville)==2) and (scoville[0] + scoville[1]*2)<K :
            return -1
    return count


