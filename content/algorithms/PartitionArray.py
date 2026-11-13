class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        minNum = nums[0]
        res = 1  # 기본 배열이 한개는 이미 있는상태. 여기서 몇번 쪼개질지?
        for num in nums:
            if num - minNum > k:
                minNum = num
                res += 1
        return res