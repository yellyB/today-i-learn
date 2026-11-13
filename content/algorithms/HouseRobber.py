class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        robs = nums[:2]
        for i in range(2, len(nums)):
            robs.append(max(robs[max(0, i - 3)], robs[max(0, i - 2)]) + nums[i])
        return max(robs)

    # 현재 집을 털거면 전전전 집[i-3]이랑 전전 집[i-2]을 털어야함
    # 그 두 경우를 비교해서 큰거 저장