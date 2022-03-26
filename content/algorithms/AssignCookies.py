class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        print(g, s)
        
        gIdx, sIdx = 0, 0
        cnt = 0
        
        while gIdx<len(g) and sIdx<len(s):
            if g[gIdx] > s[sIdx]:
                sIdx += 1
            else:
                cnt += 1
                gIdx += 1
                sIdx += 1
        
        return cnt
