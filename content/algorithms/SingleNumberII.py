class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1

        for item in freq.items():
            if item[1] == 1:
                return item[0]