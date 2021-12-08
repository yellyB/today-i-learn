class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        freq = collections.defaultdict(int)
        for num in nums1:
            freq[num] += 1

        for num in nums2:
            freq[num] += 1

        for num in nums3:
            freq[num] += 1

        answer = []
        for item in freq.items():
            if item[1] >= 2:
                answer.append(item[0])

        return answer