class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        numList = nums[:]
        
        while len(numList) > 1:
            newList = []
            for i in range(len(numList)-1):
                sums = numList[i] + numList[i+1]
                newList.append(sums-10 if sums>=10 else sums)
            numList = newList
            
        return numList[0]
