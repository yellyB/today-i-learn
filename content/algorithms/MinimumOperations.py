class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        x = 0  # 이제껏 operaion에서 빼줬던 값 누적
        cnt = 0
        for num in nums:
            if num > x:
                x += num - x
                cnt += 1
        return cnt
