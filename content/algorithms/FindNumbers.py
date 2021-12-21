class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            length =len(str(num))
            if length%2==0:
                cnt += 1
        return cnt