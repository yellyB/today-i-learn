class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx = 0
        target = len(nums) - 1
        for i,num in enumerate(nums):
            if maxIdx >= i:
                maxIdx = max(maxIdx, i+num)
        return maxIdx >= target