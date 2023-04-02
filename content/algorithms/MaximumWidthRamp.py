class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        idxs = []
        for i, num in enumerate(nums):
            idxs.append([i, num])

        sortedList = sorted(idxs, key=lambda x:x[0])
        print(sortedList)
        
        
        return 0
        # 머리가 안돌아가.. 내일 이어서 풀기
