class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        sums = 0
        minLen = len(nums) + 1
        
        while end < len(nums):
            sums += nums[end]
            while sums >= target:
                minLen = min(minLen, end-start+1)
                sums -= nums[start]
                start += 1
            end += 1
            
        return minLen if minLen < len(nums)+1 else 0
