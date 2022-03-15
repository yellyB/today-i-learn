class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        product = 1
        cnt = 0
        
        while end < len(nums):
            product *= nums[end]
            while product >= k and start <= end:
                product //= nums[start]
                start += 1
            cnt += (end+1 - start)  # [end]가 k이하면 그 앞에 어디서 시작하든 전부 k이하니까. 모든 start위치를 다 더해주는거
            end += 1
            
        return cnt
