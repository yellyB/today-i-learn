class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        idxs = []
        for i, num in enumerate(nums):
            idxs.append([i, num])

        sortedList = sorted(idxs, key=lambda x:x[1])  # value 기준으로 정렬하고

        minIdx = float('inf')
        maxWidth = 0

        for i in range(len(sortedList)):
            # 정렬한 value 를 오름차순으로 따라가다보면, width가 최대가 되려면 인덱스가 가장 작아야함.
            # 어쨌든 value로 정렬했으니까 value는 갈수록 커짐. 인덱스만 작은거 기억해놓으면 됨
            gap = sortedList[i][0] - minIdx
            maxWidth = max(maxWidth, gap)
            minIdx = min(minIdx, sortedList[i][0])
        
        return maxWidth
