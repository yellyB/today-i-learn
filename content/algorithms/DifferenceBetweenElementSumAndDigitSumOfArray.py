class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # 이게 더 빠름
        res = 0
        for num in nums:
            res += num
            while num != 0:
                res -= abs(num%10)
                num //= 10

        return res

        # sumOfElement = sum(nums)
        # sumOfDigits = sum(map(int,''.join(map(str, nums))))

        # return abs(sumOfElement - sumOfDigits)