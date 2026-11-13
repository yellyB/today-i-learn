class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        median = 0

        # 길이가 짝수면 중간꺼2개고르고  / 홀수면 걍 가운데꺼 고름 됨
        if length % 2 == 0:
            median = (nums1[length // 2 - 1] + nums1[length // 2]) / 2
            pass
        else:
            median = nums1[length // 2]

        return float(median)