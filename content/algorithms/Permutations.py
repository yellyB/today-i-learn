class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def func(idx):
            if idx == len(nums): answer.append(nums[:])
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                func(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]
        nums.sort()
        func(0)
        return answer
