class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        numsCopy = nums[:]

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] = nums[i - 1] + nums[i]
        case1 = max(nums)

        for i in range(1, len(numsCopy)):
            if numsCopy[i - 1] < 0:
                numsCopy[i] = numsCopy[i - 1] + numsCopy[i]

        # 숫자가 전부 마이너스인 경우는 total에서 최소값을 빼면 0이 나와버림 (ex: [-2,-3,-1] )
        # 그래서 total이랑 최소값이 같은 경우는 nums에서 그나마 최대값을 구함
        case2 = total - min(numsCopy) if total != min(numsCopy) else max(numsCopy)

        return max(case1, case2)

    # 53. Maximum Subarray이랑 비슷
    # case1: 가장 큰 합이 끊어지지 않고 있어 53문제의 반대로 단순하게 구하면 됨
    # case2: 가장 큰 합이 앞과 뒤에 나뉘어 있어 [총 합 - minSubArray]으로 구해야 함
    # 53문제는 가장 큰 부분배열을 구했지만 얘는 끝-시작이 이어져 있음
    # 그러니 가장 작은 부분배열을 구해서 총 합에서 빼면 됨