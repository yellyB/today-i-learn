class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len (nums)
        boolList = [False]*(length+1)
        answer = []
        for n in nums:
            boolList[n]=True
        for i in range (1,length+1):
            if not boolList[i]:
                answer.append (i)
        return answer