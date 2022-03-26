class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxGap = 0
        if len(nums) < 2: return maxGap
        
        nums.sort()
        for i in range(len(nums)-1):
            maxGap = max(maxGap, abs(nums[i] - nums[i+1]))
        return maxGap
