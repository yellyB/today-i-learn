class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len (nums))
        for i in range(len (nums)):
            for j in range (i):
                if nums [i]>nums [j]:
                    #print (nums [i],nums [j])
                    dp [i] = max (dp [j]+1, dp [i])
        #print (dp)
        return max (dp)