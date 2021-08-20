class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)
        cntList = [0] * (length + 1)
        answer = []
        for n in nums:
            cntList[n] += 1

        for i in range(1, length + 1):
            if cntList[i] == 2:
                answer.append(i)
        return answer