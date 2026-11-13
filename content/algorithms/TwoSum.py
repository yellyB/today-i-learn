class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        restDict = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in restDict:
                return [restDict[rest], i]
            else:
                restDict[num] = i

        # nums돌면서 타겟에서 숫자를 빼서 그 나머지값이랑 인덱스 저장
