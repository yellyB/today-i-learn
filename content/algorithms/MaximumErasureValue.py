class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 슬라이딩 윈도우.
        # 새로 들어온 애가 sub array에 있으면 걔 나올때까지 시작위치 옮기기
        maxSum = nums[0]
        sums = nums[0]
        sets = set()
        sets.add(nums[0])
        i, j = 1, 0  # 뒤, 앞
        while i<len(nums):
            if nums[i] in sets:
                sets.remove(nums[i])
                while nums[j] != nums[i]:
                    sets.remove(nums[j])
                    sums -= nums[j]
                    j += 1
                sums -= nums[j]
                j += 1
            sets.add(nums[i])
            sums += nums[i]
            maxSum = max(maxSum, sums)
            i += 1
        
        return maxSum
