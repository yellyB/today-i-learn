class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            if i % 2 == 0:  # => i가 freq란 뜻
                for k in range(nums[i]):
                    answer.append(nums[i+1])
        return answer