class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        n, m = len(text1), len(text2)
        
        def top_down(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i>=n or j>=m:
                return 0
            if text1[i] == text2[j]:
                return top_down(i+1, j+1) + 1
            memo[(i, j)] = max(top_down(i, j+1), top_down(i+1, j))
            return memo[(i, j)]
        
        return top_down(0, 0)
