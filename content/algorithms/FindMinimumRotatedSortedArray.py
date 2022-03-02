class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1
        while s < e:
            mid = (s+e)//2
            if nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid
        return nums[s]
    
    # 이진 탐색으로 중간값이
    # 끝값과 비교했을때 더 크다면 min값은 뒷부분에 있단거
