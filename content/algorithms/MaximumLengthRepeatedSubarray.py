class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        maxLen = 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1  # [0,0,0]과 [0,0,0]비교 같은 경우때문에 왼쪽 대각선 위에랑만 비교해야함 (왼쪽, 위쪽은 비교하면 ㄴㄴ)
                    maxLen = max(maxLen, dp[i][j])

        return maxLen
