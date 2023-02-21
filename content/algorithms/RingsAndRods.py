class Solution:
    def countPoints(self, rings: str) -> int:
        res = 0
        dict = defaultdict(set)
        
        for i in range(0, len(rings), 2):
            color, idx = rings[i], rings[i+1]
            dict[idx].add(color)

        for val in dict.values():
            if 'R' in val and 'G' in val and 'B' in val:
                res += 1
        
        return res
