class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        l = 0
        chance = k

        for r, num in enumerate(nums):
            if num == 0:
                chance -= 1

            while chance == -1:
                chance += (1-nums[l])
                l += 1
            maxLen = max(maxLen, r-l+1)

        return maxLen