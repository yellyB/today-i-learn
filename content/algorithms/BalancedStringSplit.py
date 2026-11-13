class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lCnt = 0
        cnt = 0
        for ss in s:
            if ss == 'R': lCnt -= 1
            else: lCnt += 1
            
            if lCnt == 0: cnt += 1
            
        return cnt
