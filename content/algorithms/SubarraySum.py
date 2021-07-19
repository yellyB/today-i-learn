class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        sums = 0  # 누적 합계
        sumDict = {0:1}  # hash
        for num in nums:
            sums = sums + num
            cnt = cnt + sumDict.get(sums-k, 0)
            sumDict[sums] = sumDict.get(sums, 0) + 1
        return cnt