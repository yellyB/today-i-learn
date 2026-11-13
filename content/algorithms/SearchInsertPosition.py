class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            half = left + (right - left) // 2
            if nums[half] == target:
                return half
            elif nums[half] < target:
                left = half + 1
            elif nums[half] > target:
                right = half

        return left