class Solution:
    def arraySign(self, nums: List[int]) -> int:
        flag = 1
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                flag *= -1
            else:
                flag *= 1
        return flag
