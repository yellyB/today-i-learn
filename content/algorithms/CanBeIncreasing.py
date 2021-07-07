class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def isIncrease(newList):
            for i in range(len(newList) - 1):
                if newList[i] >= newList[i + 1]:
                    return False
            return True

        i = 0
        while i < len(nums):
            newList = nums[:i] + nums[i + 1:]
            if isIncrease(newList):
                return True
            i += 1
        return False
