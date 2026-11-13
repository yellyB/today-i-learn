class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cntList = []
        for i in nums:
            cnt = 0
            for j in nums:
                if i > j:
                    cnt += 1
            cntList.append(cnt)
        return cntList