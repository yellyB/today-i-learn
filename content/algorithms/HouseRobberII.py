class Solution:
    def rob(self, nums: List[int]) -> int:

        def doRob(nums):
            robs = nums[:2]
            for i in range(2, len(nums)):
                robs.append(max(robs[max(0, i - 3)], robs[max(0, i - 2)]) + nums[i])
            return max(robs)

        length = len(nums)
        if length < 2: return max(nums)
        return max(doRob(nums[0:length - 1]), doRob(nums[1:length]))