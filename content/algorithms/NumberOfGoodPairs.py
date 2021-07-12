class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        cntOfNum = {}
        for num in nums:
            if num in cntOfNum:
                cntOfNum[num] += 1
            else:
                cntOfNum[num] = 1

        values = cntOfNum.values()
        for val in values:
            if val > 1:
                cnt = cnt + (val * (val - 1) // 2)
        return cnt