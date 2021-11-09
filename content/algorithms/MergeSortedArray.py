class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

        # m이 0이되면 (n은 아직 1이상인데) while문 빠져나와버려서 nums2의 숫자들이 추가되지 못함
        # 그래서 m이 0일 경우 추가 처리
        if m == 0:
            nums1[:n] = nums2[:n]

        print(nums1)

    # 둘에서 뽑아내야하는 갯수의 젤 마지막 번째 숫자를 비교
    # 그게 각 2, 3이라면 총 len=5까지의 리스트를 만들어야함
    # 그럼 nums1이랑 nums2에서 뽑아낼수 있는 젤 마지막숫자들끼리 비교해서 집어넣기
