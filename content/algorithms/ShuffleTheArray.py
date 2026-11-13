class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i, j in zip(nums[:n], nums[n:]):
            answer += [i, j]
        return answer
