class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = -1
        e = -1
        for i, n in enumerate(nums):
            if n == target:
                if s == -1: s = i  # target을 최초로 발견했을때만 s에 저장
                e = i  # e에는 target을 찾을때마다 저장
                
        return [s, e]
