class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq: freq[n] += 1
            else: freq[n] = 1
        
        sort = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        answer = []
        for i in range(k):
            answer.append(sort[i][0])
        
        return answer
