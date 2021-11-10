class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        restDict = {}
        for i, num in enumerate(numbers):
            rest = target - num
            if rest in restDict:
                return [restDict[rest], i+1]
            else:
                restDict[num] = i + 1