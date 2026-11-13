class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # 둘은 짝지어 합한 것 중 가장 큰 값이 최소가 되도록: 맨앞-맨끝 짝. 한칸씩 앞으로
        
        nums.sort()
        minMax = nums[0] + nums[-1]
        
        for i in range(1, len(nums)//2):
            minMax = max(minMax, nums[i] + nums[len(nums)-1-i])
        
        return minMax
