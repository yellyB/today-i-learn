class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            center = left + (right - left) // 2  #
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center + 1
            elif nums[center] > target:
                right = center - 1

        return -1

    # 주제에 맞게 풀기: 가운데 있는 값이 찾는 값인지 비교 -> 아니라면 대,소 비교해서 왼쪽포인터 혹은 오른쪽포인터를 1씩 조절
    #                 다시 가운데 값을 구해서 비교.