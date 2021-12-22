class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        answer = []
        nums.sort(reverse=True)
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
            pass
        sort = sorted(freq.items(), key=lambda x: x[1], reverse=False)  # 밸류:밸류 기준
        keys = sorted(freq.items(), key=lambda x: x[0], reverse=False)  # 키:밸류 기준
        print(sort)
        for item in sort:
            answer.extend([item[0]] * item[1])
        return answer