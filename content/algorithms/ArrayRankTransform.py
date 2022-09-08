class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {}
        rank = []
        
        for i, s in enumerate(sorted(set(arr))):
            dic[s] = i
            
        
        for a in arr:
            rank.append(dic[a]+1)
        
        return rank
