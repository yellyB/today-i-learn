class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0

        for i in range(1, len(nums)):
            if nums[i] != 0 and nums[pointer] == 0:
                nums[i], nums[pointer] = nums[pointer], nums[i]

            # 포인터는 젤 처음 나오는 0의 인덱스여야함
            # 매 턴마다 포인터를 증가시키면 연속되는 0이 나올경우
            # 두번째 0으로 가버림
            if nums[pointer] != 0: pointer += 1

        # pointer와 i로 비교
        # pointer에는 제일 처음 나오는 0을, i에는 그 0묶음 다음의 첫 양수를 가리키고 있어야함