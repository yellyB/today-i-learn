class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        rightSum = [0]
        N = len(nums)
        for i in range(N-1):
            leftSum.append(leftSum[-1] + nums[i])
            rightSum.append(rightSum[-1] + nums[N-1-i])
            
        
        res = []
        for i in range(N):
            res.append(abs(leftSum[i] - rightSum[N-1-i]))
        
        return res
