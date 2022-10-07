class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        cur = ord('a')
        for w in word:
            diff = abs(cur-ord(w))
            res += min(diff, 26-diff)
            cur = ord(w)
            res += 1
        
        return res
