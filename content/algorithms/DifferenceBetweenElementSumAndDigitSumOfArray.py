class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sumOfElement = sum(nums)
        sumOfDigits = sum(map(int,''.join(map(str, nums))))

        return abs(sumOfElement - sumOfDigits)