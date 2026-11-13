class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def recursion(sIdx, pIdx):
            if len(p) <= pIdx:  # p가 끝이면
                return sIdx == len(s)  # s도 비교 끝났는지 확인
            if len(s) <= sIdx:  # s가 끝이면
                return p[pIdx] == '*' and pIdx==len(p)-1 and recursion(sIdx, pIdx+1)  # p의 
            
            if p[pIdx] == '.':
                return recursion(sIdx+1, pIdx+1)
            elif p[pIdx] == '*':
                return recursion(sIdx+1, pIdx) or recursion(sIdx+1, pIdx+1)
            else:
                if s[sIdx] != p[pIdx]:
                    return False
                return recursion(sIdx+1, pIdx+1)
        
        return recursion(0, 0)
