class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = nums[k - 1] - nums[0]

        for i in range(1, len(nums) - k + 1):
            diff = min(diff, nums[i + k - 1] - nums[i])

        return diff

    # 정렬한 후 i+k번째 빼기 i번째 해서 작은걸 답으로 갱신한다