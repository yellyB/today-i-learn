class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for num in nums:
            for i in range(len(answer)):
                answer.extend([answer[i]+[num]])
        return answer