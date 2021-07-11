class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums, reverse=True) == nums:
            nums[:] = sorted(nums)
            return
        i = len(nums) - 2
        while i > 0 and nums[i] >= nums[i + 1]:  # 같은 숫자일때도 넘어가야되니까 i-- 해줘야함
            i -= 1
        j = len(nums) - 1
        while j > 0:
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[:] = nums[:i + 1] + sorted(nums[i + 1:])
                return
            j -= 1

