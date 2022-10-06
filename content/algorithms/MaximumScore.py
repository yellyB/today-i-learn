class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # 계속해서 가장 큰 두개 빼내면 됨
        score = 0
        q = [-a,-b,-c]  # 힙큐는 작은 순서기 때문에 마이너스 붙여서 큰수부터 비교할 수 있도록 해줌
        heapify(q)
        
        while len(q) > 1:
            a = heappop(q)
            b = heappop(q)
            a += 1
            b += 1
            if a < 0: heappush(q, a)
            if b < 0: heappush(q, b)
            
            score += 1
        return score
