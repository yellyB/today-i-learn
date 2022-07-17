class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        wDict = defaultdict(int)
        for t in text:
            wDict[t] += 1
            
        res = float('inf')
        for w in 'ban':
            res = min(res, wDict[w])
        for w in 'lloo':
            res = min(res, wDict[w] // 2)
            
        
        return res
