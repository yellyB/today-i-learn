class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, x):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x: left = mid + 1
                else: right = mid
            return right
        
        
        s = binarySearch(nums, target)
        e = binarySearch(nums, target+1) - 1
        
        if s > e: return [-1, -1]  # 못찾았으면
        
        return [s, e]
    
    # - target보다 1 큰 수의 위치 찾아서 -1하면 target이 위치한 가장 마지막 위치임
    # - 이진탐색할때 중복되는 숫자들에서 첫째 위치 찾으려면
    #   왼, 오 두 포인터 비교해서 while문 끝까지 돌림 됨
