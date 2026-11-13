class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        while s < e:
            mid = (s+e)//2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            else:
                if nums[mid] < nums[mid+1]:
                    s = mid+1
                else:
                    e = mid
                    
        # 바로 s를 리턴하지 않는 이유: len이 2 이하일 경우 때문
        return s if nums[s] >= nums[e] else e
